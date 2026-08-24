import PyPDF2
import os
import sys

def compress_pdf(input_path, output_path):
    try:
        with open(input_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()
            
            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
        
        original_size = os.path.getsize(input_path) / 1024 / 1024
        compressed_size = os.path.getsize(output_path) / 1024 / 1024
        print(f"原文件大小: {original_size:.2f} MB")
        print(f"压缩后大小: {compressed_size:.2f} MB")
        print(f"节省: {(original_size - compressed_size):.2f} MB")
        
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python compress_pdf.py <输入文件> [输出文件]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.pdf', '_compressed.pdf')
    
    compress_pdf(input_file, output_file)
