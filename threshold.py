
import matplotlib.pyplot as plt
import numpy as np

# Giả sử bạn đã có một danh sách các giá trị sim cosine và nhãn tương ứng
# Đây chỉ là ví dụ, bạn cần thay thế nó bằng dữ liệu thực tế của mình.
def plot_result_cosine_sim(similarities, labels, pos_label = 1, neg_label = 0):
    print("PLot:")
    # Phân loại các giá trị sim cosine theo nhãn
    same_speaker = [similarity for similarity, label in zip(similarities, labels) if label == pos_label]
    different_speaker = [similarity for similarity, label in zip(similarities, labels) if label == neg_label]

    # Vẽ biểu đồ
    plt.hist(same_speaker, bins=20, alpha=0.5, label='Same Speaker')
    plt.hist(different_speaker, bins=20, alpha=0.5, label='Different Speaker')

    # Đặt nhãn và tiêu đề cho biểu đồ
    plt.xlabel('Cosine Similarity')
    plt.ylabel('Frequency')
    plt.title('Speaker Verification Test')
    plt.legend()
    plt.tight_layout()

    # Hiển thị biểu đồ
    plt.show()

if __name__ == '__main__':
    def main(): 
        x = [1, 2, 3, 4, 5]
        y = [10, 20, 15, 25, 30]

        plt.plot(x, y)
        plt.xlabel('X-axis label')
        plt.ylabel('Y-axis label')
        plt.title('Simple Line Chart')
        plt.show()
        return
    main()