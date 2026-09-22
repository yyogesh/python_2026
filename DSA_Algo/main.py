# Python ==> programming, database, API
# DSA list, set, tuple, dict
# Algo 
# Principal
# Design Pattern

# Python DSA — FAANG Interview Prep Course


## Phase 1: Foundations (Classes 1–6)
1. Big-O, time/space complexity — deriving it live, not memorizing it
2. Python built-in operation costs (list/dict/set/tuple internals)
3. Recursion — mental model, call stack tracing
4. Recursion practice — factorial, fib, sum patterns, base case bugs
5. Recursion → backtracking bridge (simple subset intro)
6. Foundations review + timed problem set

## Phase 2: Arrays & Hashing (Classes 7–13)
7. Array basics — in-place ops, rotation
8. **Two Sum**, **Contains Duplicate** — hash map / set patterns
9. **Group Anagrams**, **Top K Frequent Elements** — frequency maps, bucket sort/heap
10. **Product of Array Except Self** — prefix/suffix pass technique
11. **Longest Consecutive Sequence** — hash set boundary trick
12. Sorting algorithms — bubble → merge → quick (when Python's `sorted()` is enough)
13. Arrays & Hashing mock round + review

## Phase 3: Two Pointers & Sliding Window (Classes 14–19)
14. **Valid Palindrome** — inward two-pointer scanning
15. **3Sum**, **Container With Most Water** — sort + two-pointer sweep
16. **Trapping Rain Water** — two pointers / monotonic stack
17. **Longest Substring Without Repeating Characters** — dynamic sliding window
18. **Minimum Window Substring** — frequency-constrained window
19. Two Pointers & Sliding Window mock round

## Phase 4: Stacks & Monotonic Stack (Classes 20–23)
20. **Valid Parentheses**, **Min Stack** — LIFO + O(1) auxiliary tracking
21. **Evaluate Reverse Polish Notation** — postfix arithmetic
22. **Daily Temperatures**, **Largest Rectangle in Histogram** — monotonic stack
23. Stack mock round + review

## Phase 5: Binary Search (Classes 24–27)
24. **Binary Search** (classic) — templates that avoid off-by-one bugs
25. **Search a 2D Matrix**, **Find Minimum in Rotated Sorted Array**
26. **Search in Rotated Sorted Array**, **Koko Eating Bananas** — binary search on answer space
27. **Median of Two Sorted Arrays** — partition-based binary search (hard)

## Phase 6: Linked Lists (Classes 28–32)
28. **Reverse Linked List**, **Merge Two Sorted Lists**
29. **Linked List Cycle** — Floyd's Tortoise and Hare
30. **Remove Nth Node From End**, **Reorder List**
31. **Merge k Sorted Lists** — heap / divide-and-conquer
32. **LRU Cache** — doubly linked list + hash map (real-world relevance)

## Phase 7: Trees & BSTs (Classes 33–40)
33. **Invert Binary Tree**, **Maximum Depth of Binary Tree**
34. **Diameter of Binary Tree** — post-order subtree aggregation
35. **Binary Tree Level Order Traversal** — BFS with queue
36. **Validate Binary Search Tree** — range-propagation DFS
37. **Lowest Common Ancestor** (BST & BT)
38. **Construct Binary Tree from Preorder/Inorder**
39. **Binary Tree Maximum Path Sum** — bottom-up global max
40. **Serialize and Deserialize Binary Tree** + Trees mock round

## Phase 8: Tries & Heaps (Classes 41–44)
41. **Implement Trie**, **Design Add and Search Words**
42. **Word Search II** — backtracking + Trie
43. **Kth Largest Element**, **Task Scheduler**
44. **Find Median from Data Stream** — dual-heap balance

## Phase 9: Graphs (Classes 45–51)
45. Graph representation — adjacency list/matrix, when to use which
46. **Number of Islands**, **Clone Graph**
47. **Pacific Atlantic Water Flow**, **Rotting Oranges** — multi-source BFS/DFS
48. **Course Schedule I & II** — topological sort (Kahn's / DFS cycle detection)
49. **Redundant Connection** — Union-Find (Disjoint Set)
50. **Word Ladder** — BFS shortest path in state-space graph
51. **Network Delay Time** — Dijkstra's algorithm + Graphs mock round

## Phase 10: Backtracking (Classes 52–54)
52. **Subsets & Subsets II**, **Permutations**
53. **Combination Sum**, **Generate Parentheses**
54. **Word Search**, **N-Queens** + mock round

## Phase 11: Dynamic Programming (Classes 55–59)
55. DP mental model — memoization vs tabulation
56. **1D DP:** Climbing Stairs, House Robber I/II, Coin Change
57. **1D DP:** Longest Increasing Subsequence, Word Break
58. **2D DP:** Unique Paths, Longest Common Subsequence, Edit Distance
59. **2D DP:** Buy/Sell Stock with Cooldown, 0/1 Knapsack, Burst Balloons + mock round

## Phase 12: Intervals, Greedy, Bit Manipulation (Classes 60–63)
60. **Merge Intervals**, **Insert Interval**, **Non-overlapping Intervals**
61. **Meeting Rooms II**, **Jump Game I/II**, **Gas Station**
62. **Single Number** (XOR), **Number of 1 Bits**, **Counting Bits**, **Reverse Bits**
63. **Set Matrix Zeroes**, **Rotate Image** — in-place matrix tricks

## Phase 13: Interview Simulation & Wrap-up (Classes 64–65)
64. Pattern recognition drill — map any problem statement to its technique, across ALL topics
65. Full mock interview + weak-area review + resume-ready problem sheet

---

### Notes for delivery
- **65 classes total** gives full beginner→advanced depth *and* constant interview practice (mock rounds every 1–2 phases, not saved for the end).
- **If you must compress:** drop Phase 12 (Intervals/Greedy/Bit Manipulation) to a single combined class — lowest interview frequency of the set, though still asked at Amazon (intervals) and Google/Meta (bit manipulation).
- **If you have even more time:** double up mock interview rounds, and add a "review + re-attempt" class after each phase for problems students got stuck on.
- Give 3–5 take-home problems after every class — 40 min live isn't enough reps alone; retention comes from spaced repetition on these patterns.
- Difficulty is layered so Easy problems open each pattern before Medium/Hard variants — this is what builds real confidence instead of memorized answers.

---

## Appendix: Full Pattern → Problem Bank
Quick reference — every problem in the course, grouped by pattern, with difficulty and the core technique tested.

### 1. Arrays & Hashing
| Problem | Difficulty | Technique |
|---|---|---|
| Two Sum | Easy | Hash map lookup for complements |
| Contains Duplicate | Easy | Set-based existence check |
| Group Anagrams | Medium | Frequency map / sorted key |
| Top K Frequent Elements | Medium | Bucket sort / Min-Heap |
| Product of Array Except Self | Medium | Prefix & suffix product passes |
| Longest Consecutive Sequence | Medium | Hash set boundary detection |

### 2. Two Pointers & Sliding Window
| Problem | Difficulty | Technique |
|---|---|---|
| Valid Palindrome | Easy | Inward two-pointer scan |
| 3Sum | Medium | Sort + two-pointer sweep |
| Container With Most Water | Medium | Greedy two-pointer bounding |
| Trapping Rain Water | Hard | Two pointers / monotonic stack |
| Longest Substring Without Repeating Characters | Medium | Dynamic sliding window |
| Minimum Window Substring | Hard | Frequency-constrained window |

### 3. Stack & Monotonic Stack
| Problem | Difficulty | Technique |
|---|---|---|
| Valid Parentheses | Easy | LIFO token matching |
| Min Stack | Medium | O(1) auxiliary min tracking |
| Evaluate Reverse Polish Notation | Medium | Postfix arithmetic |
| Daily Temperatures | Medium | Monotonic decreasing stack |
| Largest Rectangle in Histogram | Hard | Monotonic stack, bounding bars |

### 4. Binary Search
| Problem | Difficulty | Technique |
|---|---|---|
| Binary Search | Easy | Classic logarithmic search |
| Search a 2D Matrix | Medium | Coordinate mapping on sorted grid |
| Find Minimum in Rotated Sorted Array | Medium | Modified binary search |
| Search in Rotated Sorted Array | Medium | Pivot-aware branching |
| Koko Eating Bananas | Medium | Binary search on answer space |
| Median of Two Sorted Arrays | Hard | Partition-based binary search |

### 5. Linked Lists
| Problem | Difficulty | Technique |
|---|---|---|
| Reverse Linked List | Easy | Iterative pointer manipulation |
| Merge Two Sorted Lists | Easy | Two-pointer splice |
| Linked List Cycle | Easy | Floyd's Tortoise and Hare |
| Remove Nth Node From End of List | Medium | Two-pointer offset gap |
| Reorder List | Medium | Find middle, reverse half, weave |
| Merge k Sorted Lists | Hard | Priority queue / divide-and-conquer |
| LRU Cache | Medium/Hard | Doubly linked list + hash map |

### 6. Trees & Binary Search Trees
| Problem | Difficulty | Technique |
|---|---|---|
| Invert Binary Tree | Easy | Recursive traversal |
| Maximum Depth of Binary Tree | Easy | DFS/BFS depth tracking |
| Diameter of Binary Tree | Easy | Post-order height aggregation |
| Binary Tree Level Order Traversal | Medium | Queue-based BFS |
| Validate Binary Search Tree | Medium | Range-propagation DFS |
| Lowest Common Ancestor (BST/BT) | Medium | Tree partitioning search |
| Construct Binary Tree from Preorder/Inorder | Medium | Recursive divide-and-conquer |
| Binary Tree Maximum Path Sum | Hard | Bottom-up global max tracking |
| Serialize and Deserialize Binary Tree | Hard | Pre-order/level-order encoding |

### 7. Tries & Heaps
| Problem | Difficulty | Technique |
|---|---|---|
| Implement Trie (Prefix Tree) | Medium | Prefix-tree node construction |
| Design Add and Search Words Data Structure | Medium | Trie + wildcard DFS |
| Word Search II | Hard | Backtracking matrix + Trie |
| Kth Largest Element in an Array | Medium | Min-Heap / QuickSelect |
| Task Scheduler | Medium | Max-Heap / Greedy interval packing |
| Find Median from Data Stream | Hard | Dual-heap balance |

### 8. Backtracking
| Problem | Difficulty | Technique |
|---|---|---|
| Subsets & Subsets II | Medium | Power-set generation, dedup |
| Combination Sum | Medium | Branch exploration with reuse |
| Permutations | Medium | Factorial state exploration |
| Generate Parentheses | Medium | Constrained recursive construction |
| Word Search | Medium | Grid DFS with visited-cell backtrack |
| N-Queens | Hard | Row placement, diagonal collision sets |

### 9. Graphs
| Problem | Difficulty | Technique |
|---|---|---|
| Number of Islands | Medium | Grid connected-component DFS/BFS |
| Clone Graph | Medium | Traversal + old-to-new node map |
| Pacific Atlantic Water Flow | Medium | Multi-source reverse BFS/DFS |
| Rotting Oranges | Medium | Multi-source BFS propagation |
| Course Schedule I & II | Medium | Topological sort (Kahn's/DFS) |
| Redundant Connection | Medium | Union-Find (Disjoint Set) |
| Word Ladder | Hard | BFS shortest path in state-space |
| Network Delay Time | Medium | Dijkstra's algorithm |

### 10. Dynamic Programming — 1D
| Problem | Difficulty | Technique |
|---|---|---|
| Climbing Stairs | Easy | Fibonacci state transitions |
| House Robber & House Robber II | Medium | Linear vs circular decision DP |
| Coin Change | Medium | Unbounded knapsack, min coins |
| Longest Increasing Subsequence | Medium | O(n²) DP or O(n log n) patience sort |
| Word Break | Medium | Substring prefix-matching DP |

### 10b. Dynamic Programming — 2D / Multidimensional
| Problem | Difficulty | Technique |
|---|---|---|
| Unique Paths | Medium | Grid path counting |
| Longest Common Subsequence | Medium | 2D string matching matrix |
| Best Time to Buy/Sell Stock with Cooldown | Medium | State-machine DP |
| 0/1 Knapsack / Partition Equal Subset Sum | Medium | Target-sum boolean DP |
| Edit Distance | Hard | String transformation cost matrix |
| Burst Balloons | Hard | Matrix-chain / interval DP |

### 11. Intervals & Greedy
| Problem | Difficulty | Technique |
|---|---|---|
| Merge Intervals | Medium | Sort intervals by start time |
| Insert Interval | Medium | Overlapping range handling |
| Non-overlapping Intervals | Medium | Greedy sort by end time |
| Meeting Rooms II | Medium | Min-heap of meeting end times |
| Jump Game & Jump Game II | Medium | Greedy furthest-reach tracking |
| Gas Station | Medium | Single-pass running deficit |

### 12. Bit Manipulation & Math
| Problem | Difficulty | Technique |
|---|---|---|
| Single Number | Easy | Bitwise XOR cancellation |
| Number of 1 Bits | Easy | Brian Kernighan's algorithm |
| Counting Bits | Easy | DP with bit shifts |
| Reverse Bits | Easy | Bitmask shifts/reconstitution |
| Set Matrix Zeroes | Medium | In-place marker via first row/col |
| Rotate Image | Medium | Transpose + column reversal |

**Total: 65 problems** mapped across 12 patterns — every problem is placed in a specific class in the schedule above, so nothing here is extra homework beyond what's already taught live.







