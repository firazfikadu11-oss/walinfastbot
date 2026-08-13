from pathlib import Path
import zipfile

out = Path("/mnt/data/WalinFast_RocketRise")
out.mkdir(exist_ok=True)

bot = r'''import os
import threading
from flask import Flask, Response
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEB_APP_URL = os.environ.get("WEB_APP_URL")

app = Flask(__name__)

HTML = r"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Walin Fast</title>
<style>
body{margin:0;background:#0b1020;color:#fff;font-family:Arial;text-align:center}
.wrap{max-width:520px;margin:auto;padding:18px}.top{display:flex;justify-content:space-between}
.card{background:#141d35;border-radius:20px;padding:18px;margin-top:16px}
.arena{height:330px;background:linear-gradient(#182a52,#0b1020);border-radius:16px;position:relative;overflow:hidden}
.mult{font-size:42px;font-weight:bold;padding-top:18px}.rocket{font-size:55px;position:absolute;left:50%;bottom:25px;transform:translateX(-50%)}
button{width:100%;padding:15px;border:0;border-radius:14px;font-size:18px;font-weight:bold;background:#35d39a;color:#06120d}
.stats{display:flex;gap:10px;margin-top:12px}.stat{flex:1;background:#1b2744;border-radius:12px;padding:10px}
.small{opacity:.7;font-size:12px}
</style></head>
<body><div class="wrap">
<div class="top"><h2>🚀 Walin Fast</h2><div>🪙 <span id="points">1000</span></div></div>
<div class="card"><div class="arena"><div class="mult" id="mult">1.00x</div><div class="rocket" id="rocket">🚀</div></div>
<p id="status">START cuqaasi!</p><button id="start">START GAME</button>
<div class="stats"><div class="stat"><div class="small">BEST</div><b id="best">0</b></div>
<div class="stat"><div class="small">SCORE</div><b id="score">0</b></div></div></div>
<div class="card small">Virtual points only — real-money betting/cash-out hin qabu.</div>
</div>
<script>
let points=+localStorage.wfPoints||1000,best=+localStorage.wfBest||0,running=false,t=0,timer;
const e=id=>document.getElementById(id);
function render(){e('points').textContent=points;e('best').textContent=best}
function end(score){clearInterval(timer);running=false;e('start').disabled=false;best=Math.max(best,score);points+=Math.min(50,Math.floor(score/20));localStorage.wfBest=best;localStorage.wfPoints=points;e('status').textContent='💥 Round over! Score: '+score;e('rocket').style.bottom='25px';e('mult').textContent='1.00x';render()}
function start(){if(running)return;running=true;t=0;e('start').disabled=true;e('status').textContent='Rocket is rising...';let crash=2.2+Math.random()*5.8;
timer=setInterval(()=>{t+=.08;let m=1+Math.pow(t,1.35)*.18;let s=Math.floor(m*100);e('mult').textContent=m.toFixed(2)+'x';e('score').textContent=s;e('rocket').style.bottom=Math.min(250,25+t*30)+'px';if(t>=crash)end(s)},80)}
e('start').onclick=start;render();
</script></body></html>"""

@app.get("/")
def home():
    return Response(HTML, mimetype="text/html")

@app.get("/health")
def health():
    return "OK", 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard=[[InlineKeyboardButton("🚀 Play Walin Fast", web_app=WebAppInfo(url=WEB_APP_URL))]]
    await update.message.reply_text(
        "🎮 Walin Fast — Rocket Rise\n\nVirtual points qofa. START cuqaasiitii taphadhu!",
        reply_markup=InlineKeyboardMarkup(keyboard))

def run_web():
    port=int(os.environ.get("PORT","8080"))
    app.run(host="0.0.0.0",port=port,threaded=True)

def main():
    if not BOT_TOKEN: raise RuntimeError("BOT_TOKEN hin jiru.")
    if not WEB_APP_URL: raise RuntimeError("WEB_APP_URL hin jiru.")
    threading.Thread(target=run_web,daemon=True).start()
    bot=Application.builder().token(BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start",start))
    print("Walin Fast Bot started...")
    bot.run_polling(drop_pending_updates=True)

if __name__=="__main__":
    main()
'''
(out/"bot.py").write_text(bot, encoding="utf-8")
(out/"requirements.txt").write_text("Flask\npython-telegram-bot\n", encoding="utf-8")
zip_path="/mnt/data/WalinFast_RocketRise.zip"
with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    z.write(out/"bot.py","bot.py")
    z.write(out/"requirements.txt","requirements.txt")
print(zip_path)
