class KSortedLists:
    def mergeKLists(self, lists):
        interval = 1
        while (interval < len(lists)):
            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if len(lists) > 0 else lists

    def merge2Lists(self, list1, list2):
        i = j = 0
        result = []
        while (i < len(list1) and j < len(list2)):
            if(list1[i] < list2[j]):
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        while(i <= len(list1) - 1):
            result.append(list1[i])
            i += 1
            # k += 1
        while(j <= len(list2) - 1):
            result.append(list2[j])
            j += 1
            # k += 1
        return result


print(KSortedLists().merge2Lists([1, 4, 23], [2, 3, 3, 3, 4]))
print(KSortedLists().mergeKLists(
    [[1, 4, 23], [2, 3, 3, 3, 4], [1, 3, 4, 7, 8]]))
