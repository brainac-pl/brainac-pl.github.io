"""Pobiera dzienne zamknięcia ^SP500TR (S&P 500 Total Return) z Yahoo Finance do data/sp500tr.csv."""
import sys
import yfinance as yf
 
df = yf.Ticker("^SP500TR").history(start="1988-01-01", auto_adjust=False)
df = df.dropna(subset=["Close"])
if len(df) < 1000:  # zabezpieczenie: nie nadpisuj dobrego pliku pustym wynikiem
    sys.exit(f"Za mało danych ({len(df)} wierszy) - przerywam")
with open("data/sp500tr.csv", "w", encoding="utf-8") as f:
    f.write("Date,Close\n")
    for ts, row in df.iterrows():
        f.write(f"{ts.strftime('%Y-%m-%d')},{row['Close']:.4f}\n")
print(f"Zapisano {len(df)} wierszy, ostatni: {df.index[-1].date()}")
