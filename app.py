from flask import Flask, jsonify
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route('/kurser')
def kurser():
    aksjer = {
        "SMOP": "SMOP.OL",
        "ENDUR": "ENDUR.OL",
        "SDSD": "SDSD.OL",
        "KOG": "KOG.OL",
        "EQNR": "EQNR.OL",
        "DNB": "DNB.OL",
        "MOWI": "MOWI.OL",
        "ORK": "ORK.OL"
    }
    resultat = {}
    for navn, ticker in aksjer.items():
        try:
            data = yf.Ticker(ticker)
            info = data.fast_info
            resultat[navn] = {
                "kurs": round(info.last_price, 2),
                "endring_pct": round(info.last_price / info.previous_close * 100 - 100, 2)
            }
        except:
            resultat[navn] = {"kurs": "N/A", "endring_pct": "N/A"}
    resultat["oppdatert"] = datetime.now().strftime("%H:%M:%S")
    return jsonify(resultat)

if __name__ == '__main__':
    app.run()
