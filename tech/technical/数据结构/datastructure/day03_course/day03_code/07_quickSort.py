"""
python实现快速排序
"""

def quick_sort(li, first, last):
    # 递归出口
    if first >= last:
        return

    split_pos = sort(li, first, last)
    # 递归思想
    quick_sort(li, first, split_pos-1)
    quick_sort(li, split_pos+1, last)

def sort(li, first, last):
    """
    :param li: 源列表(从头到尾操作的列表)
    :param first: 基准值的下标索引
    :param last: 最后一个元素的下标索引
    :return: 基准值的正确位置
    """
    mid = li[first]
    lcur = first + 1
    rcur = last
    while True:
        # 左游标右移
        while lcur <= rcur and li[lcur] <= mid:
            lcur += 1
        # 右游标左移
        while lcur <= rcur and li[rcur] >= mid:
            rcur -= 1
        # 判断是交换哪个位置
        if lcur <= rcur:
            li[lcur], li[rcur] = li[rcur],li[lcur]
        else:
            li[first],li[rcur] = li[rcur], li[first]
            # 基准值正确位置,同时又是将列表分成
            # 左右两部分的值
            return rcur

if __name__ == '__main__':
    li = [6, 333, 5, 666, 2, 3, 666, 1, 8, 7, 2, 8, 333, 4]
    quick_sort(li, 0, len(li)-1)
    print(li)













