"""Starter test suite — proves the package imports post-restructure and a few core
algorithms are correct. Coverage expands module-by-module as the learning layer lands."""

from __future__ import annotations

import metabeaver
from metabeaver.InterviewQuestions.Arrays.twoSum import (
    twoSumWithHashmap,
    twoSumWithTwoPointers,
)
from metabeaver.SortingAlgorithms.mergeSort import mergeSort


def test_package_imports():
    assert metabeaver is not None


def test_two_sum_hashmap_finds_pair():
    assert twoSumWithHashmap([2, 7, 11, 15], 9) == [0, 1]
    assert twoSumWithHashmap([3, 2, 4], 6) == [1, 2]


def test_two_sum_two_pointers_finds_pair():
    assert twoSumWithTwoPointers([2, 7, 11, 15], 9) == [0, 1]
    assert twoSumWithTwoPointers([3, 2, 4], 6) == [1, 2]


def test_merge_sort_orders_in_place():
    data = [5, 3, 8, 1, 9, 2, 5]
    mergeSort(data)
    assert data == sorted([5, 3, 8, 1, 9, 2, 5])


def test_merge_sort_handles_empty_and_singleton():
    empty: list[int] = []
    mergeSort(empty)
    assert empty == []
    single = [42]
    mergeSort(single)
    assert single == [42]
