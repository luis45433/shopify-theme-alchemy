from pathlib import Path

from fontTools.ttLib import TTFont

def main(sourcefile, fontname):
    f = TTFont(sourcefile)
    f.flavor='woff2'
    f.save(f'assets/{fontname}.woff2')
    f.close()

if __name__ == '__main__':
    ttf_file = Path(r'C:\Users\leoma\Documents\Shopify\Just Sunday Demo.ttf')
    fontname = 'JustSunday'
    main(ttf_file, fontname)
