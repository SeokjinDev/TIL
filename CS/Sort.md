# Sort Algorithm

## O(n^2)
* **Bubble Sort**   
    이웃하는 숫자 중 작은 수를 앞으로 이동시키는 것을 반복하는 정렬 알고리즘   
    정렬 후에도 순서가 바뀌지 않는 안정된 정렬이다.
    ```python 3
    # python 3
    def bubbleSort(data):
        length = len(data)
        for i in range(length-1):
            for j in range(length-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data
    ```

* **Selection Sort**   
    정렬되지 않은 데이터 중 최솟값을 정렬되지 않은 영역 가장 앞의 원소와 바꾸는 것을 반복한다.
    ```python 3
    # python 3
        def selectionSort(data):
        length = len(data)
        for i in range(length):
            minLoc = i
            for j in range(i+1, length):
                if data[j] < data[minLoc]:
                    minLoc = j
            data[i], data[minLoc] = data[minLoc], data[i]
        return data
    ```