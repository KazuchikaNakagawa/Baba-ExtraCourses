
# PDF/Aに変換するシェルスクリプト
# Ghostscriptが入っていないとエラーになります。
# 使うときは、zsh pdf2pdfa.sh [変換元PDFファイル] [変換後PDFファイル] みたいな感じで使ってください。
gs -dPDFA -dBATCH -dNOPAUSE -sColorConversionStrategy=UseDeviceIndependentColor -sDEVICE=pdfwrite -dPDFACompatibilityPolicy=2 -o $2 $1