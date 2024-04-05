# high_scores = [78, 56, 67]
# def a(high_scores):
#     print("High scores:")
#     for i in range(len(high_scores)):
#         print(f"{i+1}. {high_scores}")
# def b(high_scores):
#     high_scores.append(input(" input new score : "))
#     for i in range(len(high_scores)):
#         for j in range(len(high_scores)):
#             if high_scores[i] > high_scores[j]:
#                  high_scores[i] , high_scores[j] =  high_scores[j] , high_scores[i]
#     print("hight_scores :")
#     if len(high_scores) > 5:
#         for i in range(5):
#             print(f"{i+1}.{high_scores[i]}")
#     else :
#          for i in range(len(high_scores)):
#             print(f"{i+1}.{high_scores[i]}")
# Tạo list chứa điểm cao ban đầu
high_scores = [78, 70, 67, 56, 45]
print("High scores:")
for i, score in enumerate(high_scores, start=1):
    print(f"{i}. {score}")

def add_and_sort_new_score(scores, new_score):
    scores.append(new_score)
    scores.sort(reverse=True)
    return scores[:5]  # Chỉ lấy 5 điểm cao nhất

new_score = int(input("Input new score: "))

# Thêm điểm mới và chỉ hiển thị 5 điểm cao nhất
top_5_scores = add_and_sort_new_score(high_scores, new_score)

print("High scores:")
for i, score in enumerate(top_5_scores, start=1):
    print(f"{i}. {score}")


                

     
    


