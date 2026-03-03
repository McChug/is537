function mergeSort(nums1, nums2) {
  let destPointer = nums1.length + nums2.length - 1;

  let next1 = nums1.length - 1;
  let next2 = nums2.length - 1;

  while (next1 && next2) {
    if (nums1[next1] > nums2[next2]) {
      nums1[destPointer] = nums1[next1];
      next1 -= 1;
    } else {
      nums1[destPointer] = nums2[next2];
      next2 -= 1;
    }

    destPointer -= 1;
  }

  return nums1;
}

nums1 = [1, 1, 2, 4, 5, 7];
nums2 = [3, 4, 6, 6, 7, 8, 9];
console.log(mergeSort(nums1, nums2));
