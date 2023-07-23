# Lab 2: Text Similarity Measurement

### Yêu cầu:

Vui lòng cài đặt các độ đo tương tự sử dụng trong so sánh chuỗi mà không dùng thư viện hỗ trợ (code from scratch). Các độ đo bao gồm:

- Levenshtein. 

- Hamming distance.

- Jaccard

So sánh độ tương tự giữa 2 câu:

- Bag of Word

- TF-IDF

- Cosine

### Bài tập

Bài tập này có 4 files .py: 
	
	+ main: chương trình sẽ chạy trong file này 
	
	+ nlmetrics: file này định nghĩa các hàm cho các độ đo tương ứng, có 3 hàm:
		
		** levenshtein_distance(s1, s2): độ đo Levenshtein

		** hamming_distance(s1, s2): độ đo Hamming

		** jaccard_index(s1, s2): độ đo Jaccard

	+ nlmodels: file này định nghĩa các hàm cho các model tương ứng, có 3 hàm:

		** bag_of_words(s1, s2): model Bag-of-words

		** cosine(s1, s2): model Cosine

		** tfidf(s1, s2): model TF-IDF

	+ similarity: hàm similarity(s1, s2) tính độ tương đồng giữa hai chuỗi s1 và s2