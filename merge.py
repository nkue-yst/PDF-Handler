# 複数のPDFファイルを
# 1つのPDFファイルに統合するプログラム

from PyPDF2 import PdfFileMerger
import os
import glob

def main():
    merger = PdfFileMerger()

    merge_files = []
    i = 1
    while True:
        print("Merge file or Folder ", i, " (Type 'm' to merge.) -> ", sep='', end='')
        in_file = input()

        if in_file == 'm':
            break
        elif os.path.isfile(in_file):
            path, ext = os.path.splitext(in_file)
            if ext == '.pdf':
                merge_files.append(in_file)
                i += 1
            else:
                print("指定したファイルはPDFファイルではありません.")
        else:
            for file in glob.glob(in_file + '*.pdf'):
                merge_files.append(file)
                print("Add " + file)
                i += 1

    print("Generated file -> ", end='')
    out_file = input()
    path, ext = os.path.splitext(out_file)

    if ext != '.pdf':
        out_file = out_file + '.pdf'

    for file in merge_files:
        merger.append(file)
        print("Completed merge ", file, " to ", out_file, "...", sep='')
    
    merger.write(out_file)
    merger.close()
    print("File merge completed!!")


if __name__ == '__main__':
    main()
