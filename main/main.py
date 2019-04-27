from uncached_query import UncachedQuery
from cached_query import CachedQuery
slow = CachedQuery('hpc_network','postgres','password','192.17.100.193','5432')
slow.setup_cache('random',10)
res1 = slow.exec_query_with_cache('select * from network limit 250')
print(res1)
res2 = slow.exec_query_with_cache('select a.id,a.name,a.cpus,a.state, n.time, n.port,n.flit,f.rtr from apps a inner join network n on a.start = n.time inner join failure f on n.rtr=f.rtr')
print('Done')
res2 = slow.exec_query_with_cache('select a.id,a.name,a.cpus,a.state, n.time, n.port,n.flit,f.rtr from apps a inner join network n on a.start = n.time inner join failure f on n.rtr=f.rtr')
print('Done')
slow.close()
