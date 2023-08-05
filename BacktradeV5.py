import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import numpy as np
from scipy.signal import find_peaks

def calculate_rsi(data, period=14):
    # ... (Same as before)

def find_rsi_divergence(prices, rsi):
    price_peaks, _ = find_peaks(prices)
    rsi_peaks, _ = find_peaks(rsi)

    price_valleys, _ = find_peaks(-prices)
    rsi_valleys, _ = find_peaks(-rsi)

    price_divergence = set(price_peaks).intersection(set(rsi_valleys))
    rsi_divergence = set(rsi_peaks).intersection(set(price_valleys))

    # Calculate divergence spans (consecutive periods with divergence)
    price_divergence_spans = np.split(sorted(price_divergence), np.where(np.diff(sorted(price_divergence)) > 1)[0] + 1)
    rsi_divergence_spans = np.split(sorted(rsi_divergence), np.where(np.diff(sorted(rsi_divergence)) > 1)[0] + 1)

    # Filter out divergences that are less than 10 4-hour periods
    filtered_price_divergence = [div for div in price_divergence_spans if len(div) >= 10]
    filtered_rsi_divergence = [div for div in rsi_divergence_spans if len(div) >= 10]

    return [item for sublist in filtered_price_divergence for item in sublist], [item for sublist in filtered_rsi_divergence for item in sublist]

def plot_price_rsi(stock_name, prices, rsi, price_divergence, rsi_divergence):
    # ... (Same as before)

def main():
    # ... (Same as before)

    # Create a PDF file to store the plots
    pdf_file = "stock_plots.pdf"
    with matplotlib.backends.backend_pdf.PdfPages(pdf_file) as pdf:
        for stock_name in all_stocks:
            try:
                # ... (Same as before)

                # Find RSI divergence
                price_divergence, rsi_divergence = find_rsi_divergence(data["Close"], rsi)

                # Plot Price and RSI if divergence duration is met
                if len(price_divergence) >= 10 and len(rsi_divergence) >= 10:
                    plot_price_rsi(stock_name, data["Close"], rsi, price_divergence, rsi_divergence)
                    # Save the plot in the PDF file
                    pdf.savefig()
            except Exception as e:
                print(f"Error processing {stock_name}: {str(e)}")

    print(f"All plots saved to '{pdf_file}'.")

if __name__ == "__main__":
    main()
