"""
test ipfs api interface.

"""
import pytest
from .server import (
    VERSION, ID, PEERS
)

pytestmark = pytest.mark.asyncio(forbid_global_loop=True)

# async def test_add(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.add()
#         assert content == {}
#
# async def test_bitswap_ledger(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bitswap_ledger()
#         assert content == {}
#
# async def test_bitswap_reprovide(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bitswap_reprovide()
#         assert content == {}
#
# async def test_bitswap_stat(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bitswap_stat()
#         assert content == {}
#
# async def test_bitswap_wantlist(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bitswap_wantlist()
#         assert content == {}
#
# async def test_bitswap_unwant(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bitswap_unwant()
#         assert content == {}
#
# async def test_block_get(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.block_get()
#         assert content == {}
#
# async def test_block_put(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.block_put()
#         assert content == {}
#
# async def test_block_rm(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.block_rm()
#         assert content == {}
#
# async def test_block_stat(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.block_stat()
#         assert content == {}
#
# async def test_bootstrap_add_default(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bootstrap_add_default()
#         assert content == {}
#
# async def test_bootstrap_list(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bootstrap_list()
#         assert content == {}
#
# async def test_bootstrap_rm_all(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.bootstrap_rm_all()
#         assert content == {}
#
# async def test_cat(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.cat()
#         assert content == {}
#
# async def test_commands(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.commands()
#         assert content == {}
#
# async def test_config_edit(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.config_edit()
#         assert content == {}
#
# async def test_config_replace(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.config_replace()
#         assert content == {}
#
# async def test_config_show(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.config_show()
#         assert content == {}
#
# async def test_dag_get(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dag_get()
#         assert content == {}
#
# async def test_dag_put(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dag_put()
#         assert content == {}
#
# async def test_dag_resolve(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dag_resolve()
#         assert content == {}
#
# async def test_dht_findpeer(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dht_findpeer()
#         assert content == {}
#
# async def test_dht_findprovs(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dht_findprovs()
#         assert content == {}
#
# async def test_dht_get(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dht_get()
#         assert content == {}
#
# async def test_dht_provide(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dht_provide()
#         assert content == {}
#
# async def test_dht_put(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dht_put()
#         assert content == {}
#
# async def test_dht_query(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dht_query()
#         assert content == {}
#
# async def test_diag_cmds_clear(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.diag_cmds_clear()
#         assert content == {}
#
# async def test_diag_cmds_set_time(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.diag_cmds_set_time()
#         assert content == {}
#
# async def test_diag_sys(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.diag_sys()
#         assert content == {}
#
# async def test_dns(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.dns()
#         assert content == {}
#
# async def test_file_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.file_ls()
#         assert content == {}
#
# async def test_files_cp(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_cp()
#         assert content == {}
#
# async def test_files_flush(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_flush()
#         assert content == {}
#
# async def test_files_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_ls()
#         assert content == {}
#
# async def test_files_mkdir(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_mkdir()
#         assert content == {}
#
# async def test_files_mv(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_mv()
#         assert content == {}
#
# async def test_files_read(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_read()
#         assert content == {}
#
# async def test_files_rm(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_rm()
#         assert content == {}
#
# async def test_files_stat(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_stat()
#         assert content == {}
#
# async def test_files_write(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.files_write()
#         assert content == {}
#
# async def test_filestore_dups(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.filestore_dups()
#         assert content == {}
#
# async def test_filestore_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.filestore_ls()
#         assert content == {}
#
# async def test_filestore_verify(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.filestore_verify()
#         assert content == {}
#
# async def test_get(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.get()
#         assert content == {}
#
async def test_id(ipfs_client):
    async with ipfs_client:
        content = await ipfs_client.id()
        assert content == ID
#
# async def test_key_gen(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.key_gen()
#         assert content == {}
#
# async def test_key_list(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.key_list()
#         assert content == {}
#
# async def test_key_rename(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.key_rename()
#         assert content == {}
#
# async def test_key_rm(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.key_rm()
#         assert content == {}
#
# async def test_log_level(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.log_level()
#         assert content == {}
#
# async def test_log_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.log_ls()
#         assert content == {}
#
# async def test_log_tail(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.log_tail()
#         assert content == {}
#
# async def test_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.ls()
#         assert content == {}
#
# async def test_mount(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.mount()
#         assert content == {}
#
# async def test_name_publish(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.name_publish()
#         assert content == {}
#
# async def test_name_resolve(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.name_resolve()
#         assert content == {}
#
# async def test_object_data(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_data()
#         assert content == {}
#
# async def test_object_diff(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_diff()
#         assert content == {}
#
# async def test_object_get(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_get()
#         assert content == {}
#
# async def test_object_links(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_links()
#         assert content == {}
#
# async def test_object_new(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_new()
#         assert content == {}
#
# async def test_object_patch_add_link(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_patch_add_link()
#         assert content == {}
#
# async def test_object_patch_append_data(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_patch_append_data()
#         assert content == {}
#
# async def test_object_patch_rm_link(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_patch_rm_link()
#         assert content == {}
#
# async def test_object_patch_set_data(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_patch_set_data()
#         assert content == {}
#
# async def test_object_put(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_put()
#         assert content == {}
#
# async def test_object_stat(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.object_stat()
#         assert content == {}
#
# async def test_p2p_listener_close(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.p2p_listener_close()
#         assert content == {}
#
# async def test_p2p_listener_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.p2p_listener_ls()
#         assert content == {}
#
# async def test_p2p_listener_open(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.p2p_listener_open()
#         assert content == {}
#
# async def test_p2p_stream_close(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.p2p_stream_close()
#         assert content == {}
#
# async def test_p2p_stream_dial(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.p2p_stream_dial()
#         assert content == {}
#
# async def test_p2p_stream_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.p2p_stream_ls()
#         assert content == {}
#
# async def test_pin_add(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pin_add()
#         assert content == {}
#
# async def test_pin_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pin_ls()
#         assert content == {}
#
# async def test_pin_rm(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pin_rm()
#         assert content == {}
#
# async def test_pin_update(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pin_update()
#         assert content == {}
#
# async def test_pin_verify(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pin_verify()
#         assert content == {}
#
# async def test_ping(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.ping()
#         assert content == {}
#
# async def test_pubsub_ls(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pubsub_ls()
#         assert content == {}
#
# async def test_pubsub_peers(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pubsub_peers()
#         assert content == {}
#
# async def test_pubsub_pub(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pubsub_pub()
#         assert content == {}
#
# async def test_pubsub_sub(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.pubsub_sub()
#         assert content == {}
#
# async def test_refs_local(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.refs_local()
#         assert content == {}
#
# async def test_repo_fsck(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.repo_fsck()
#         assert content == {}
#
# async def test_repo_gc(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.repo_gc()
#         assert content == {}
#
# async def test_repo_stat(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.repo_stat()
#         assert content == {}
#
# async def test_repo_verify(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.repo_verify()
#         assert content == {}
#
# async def test_repo_version(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.repo_version()
#         assert content == {}
#
# async def test_resolve(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.resolve()
#         assert content == {}
#
# async def test_shutdown(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.shutdown()
#         assert content == {}
#
# async def test_stats_bitswap(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.stats_bitswap()
#         assert content == {}
#
# async def test_stats_bw(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.stats_bw()
#         assert content == {}
#
# async def test_stats_repo(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.stats_repo()
#         assert content == {}
#
# async def test_swarm_addrs_listen(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.swarm_addrs_listen()
#         assert content == {}
#
# async def test_swarm_addrs_local(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.swarm_addrs_local()
#         assert content == {}
#
# async def test_swarm_connect(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.swarm_connect()
#         assert content == {}
#
# async def test_swarm_disconnect(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.swarm_disconnect()
#         assert content == {}
#
# async def test_swarm_filters_add(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.swarm_filters_add()
#         assert content == {}
#
# async def test_swarm_filters_rm(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.swarm_filters_rm()
#         assert content == {}

async def test_swarm_peers(ipfs_client):
    async with ipfs_client:
        content = await ipfs_client.swarm_peers()
        assert content == PEERS

# async def test_tar_add(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.tar_add()
#         assert content == {}
#
# async def test_tar_cat(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.tar_cat()
#         assert content == {}
#
# async def test_update(ipfs_client):
#     async with ipfs_client:
#         content = await ipfs_client.update()
#         assert content == {}

async def test_version(ipfs_client):
    async with ipfs_client:
        content = await ipfs_client.version()
        assert content == VERSION
