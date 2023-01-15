def solve(n, adj):
	unvisited = set(range(1, n+1))
	starts = set()

	def dfs(start):
		to_visit = [start]
		while to_visit:
			current = to_visit.pop()
			for next in adj[current]:
				if next in unvisited:
					unvisited.remove(next)
					to_visit.append(next)

	while unvisited:
		start = unvisited.pop()
		starts.add(start)
		dfs(start)

	print(len(starts) - 1)
	root = starts.pop()
	for other in starts:
		print(root, other)

if __name__ == '__main__':
	n, m = map(int, input().split())
	adj = [set() for _ in range(n+1)]
	for _ in range(m):
		u, v = map(int, input().split())
		adj[u].add(v)
		adj[v].add(u)
	solve(n, adj)
