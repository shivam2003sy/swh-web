# Copyright (C) 2017-2018  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

# flake8: noqa

origin_info_test_data = {
    'id': 2,
    'type': 'git',
    'url': 'https://github.com/torvalds/linux'
}

origin_visits_test_data = [
 {'date': '2015-07-09T21:09:24+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 1},
 {'date': '2016-02-23T18:05:23.312045+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 2},
 {'date': '2016-03-28T01:35:06.554111+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 3},
 {'date': '2016-06-18T01:22:24.808485+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 4},
 {'date': '2016-08-14T12:10:00.536702+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 5},
 {'date': '2016-08-17T09:16:22.052065+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 6},
 {'date': '2016-08-29T18:55:54.153721+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 7},
 {'date': '2016-09-07T08:44:47.861875+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 8},
 {'date': '2016-09-14T10:36:21.505296+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 9},
 {'date': '2016-09-23T10:14:02.169862+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 10},
 {'date': '2017-02-16T07:53:39.467657+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'partial',
  'visit': 11},
 {'date': '2017-05-04T19:40:09.336451+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 12},
 {'date': '2017-09-07T18:43:13.021746+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 13},
 {'date': '2017-09-09T05:14:33.466107+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 14},
 {'date': '2017-09-09T17:18:54.307789+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 15},
 {'date': '2017-09-10T05:29:01.462971+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 16},
 {'date': '2017-09-10T17:35:20.158515+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 17},
 {'date': '2017-09-11T05:49:58.300518+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 18},
 {'date': '2017-09-11T18:00:15.037345+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 19},
 {'date': '2017-09-12T06:06:34.703343+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 20},
 {'date': '2017-09-12T18:12:35.344511+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 21},
 {'date': '2017-09-13T06:26:36.580675+00:00',
  'metadata': {},
  'origin': 2,
  'status': 'full',
  'visit': 22}
]

stub_origin_info = {
    'id': 7416001,
    'type': 'git',
    'url': 'https://github.com/webpack/webpack'
}
stub_visit_id = 10
stub_visit_unix_ts = 1493909263
stub_visit_iso_date = '2017-05-04T14:47:43+00:00'

stub_origin_visits = [
{'date': '2015-08-05T18:55:20.899865+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 1},
 {'date': '2016-03-06T12:16:26.240919+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 2},
 {'date': '2016-03-21T11:40:10.329221+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 3},
 {'date': '2016-03-29T08:05:17.602649+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 4},
 {'date': '2016-07-26T20:11:03.827577+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 5},
 {'date': '2016-08-13T04:10:22.142897+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 6},
 {'date': '2016-08-16T22:57:46.201737+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 7},
 {'date': '2016-08-17T17:58:43.346437+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 8},
 {'date': '2016-08-29T23:29:09.445945+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 9},
 {'date': '2016-09-07T13:49:15.096109+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 10},
 {'date': '2016-09-14T15:01:09.017257+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 11},
 {'date': '2016-09-23T12:29:15.921727+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 12},
 {'date': '2017-02-16T07:44:23.302439+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'partial',
  'visit': 13},
 {'date': '2017-05-04T14:47:43.228455+00:00',
  'metadata': {},
  'origin': 7416001,
  'status': 'full',
  'visit': 14}
]

stub_origin_branches = [
 {'directory': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'name': 'HEAD',
  'revision': '7bc08e1aa0b08cb23e18715a32aa38517ad34672'},
 {'directory': 'c47a824f95109ca7cafdd1c3206332a0d10df55d',
  'name': 'refs/heads/0.10',
  'revision': 'f944553c77254732c4ce22c0add32aa1f641959d'},
 {'directory': '45e31184ebb7699cd74175145c7eb11cce3f085e',
  'name': 'refs/heads/0.11',
  'revision': '0a29109a6e4579926ebc9b03a6301c61861cce62'},
 {'directory': '42346b33e2d16019490c273ff586ee88817327b3',
  'name': 'refs/heads/0.8',
  'revision': 'e42701dc6f9b035bfbb5d0fffded905d8b456db4'},
 {'directory': '828c7e9385523f852f8d4dac3cb241e319a9ce61',
  'name': 'refs/heads/0.9',
  'revision': '6c3f51e6d9491a2463ad099a2ca49255ec83ff00'},
 {'directory': '2c50e78d63bdc4441c8d2691f5729b04f0ab3ecd',
  'name': 'refs/heads/1.0',
  'revision': 'fb7958d172e1ef6fb77f23bf56818ad24e896e5c'},
 {'directory': '31a3355c4d0a464aa311c5fa11c7f8b20aede6b4',
  'name': 'refs/heads/IgnorePluginHotfix',
  'revision': 'fdc922a2fa007e71b7ec07252012ffab9a178d4a'},
 {'directory': 'e566db1fc65cb61b3799c6e0f0ad06b2406f095f',
  'name': 'refs/heads/beta',
  'revision': '40428853da5d9ce6a8751e13b5e54145337b6a7e'},
 {'directory': '0f3cf363d4184a2cc36fdbebe1657d40fad6a591',
  'name': 'refs/heads/break/add-timeout',
  'revision': '14c43e0cc54af67344f8304708ccdd7b8ab91110'},
 {'directory': '8dc14b0625b2280d630aeae9dd424054c37db820',
  'name': 'refs/heads/bugfix/child-records-cache',
  'revision': '101850c5a90dbc51f1a95813fe1fece42bc1b9dc'},
 {'directory': '08c703fdf5cdb4f9321a1e1ad616eeeb78c96670',
  'name': 'refs/heads/bugfix/disable-module-in-harmony',
  'revision': 'bebe688e6cd0cfe35b967069ddfe1ca42a83f99b'},
 {'directory': '2378f4c463a54f057e42b2e489cd641645f82517',
  'name': 'refs/heads/bugfix/dll-extension',
  'revision': '38264a092e130b83bfe521e6e35a3b3e7600f183'},
 {'directory': 'def1489e00e12ed6ed2515c782da4ed29bf7a2dc',
  'name': 'refs/heads/bugfix/order',
  'revision': '089356faa3d27c1ef4d5c9eee1c235bc8ea505ea'},
 {'directory': 'fe1f7ebe60b771b6494be316fc01c305e0ba5c3c',
  'name': 'refs/heads/bugfix/status',
  'revision': '206ef6d079515a57fbca113cbdcb53cec3def4d6'},
 {'directory': '4cb66b94d3f2438fc095271f7184ca643ce1cdc4',
  'name': 'refs/heads/ci/bench',
  'revision': '21af9e96908e62616eaf04337dfc1b69630765d9'},
 {'directory': 'c1aff7c49f9a38edb1d2e037cc401a9f9e2366ff',
  'name': 'refs/heads/dep/dependency-update',
  'revision': '0bb4b14118ce8ce745222c89c75c166f219a6193'},
 {'directory': 'b4db55e82f9d7b7a9ebc8ce6a2b511d86efb3012',
  'name': 'refs/heads/feature/emoji_presets_to_options',
  'revision': 'a6ebd61bb967d66e1573562f58b2d36893cf338d'},
 {'directory': '676474786d3e6334f1a71bf49adb1e53b0681d34',
  'name': 'refs/heads/feature/fix_errors_only_bug',
  'revision': '5dd1d0cb130032fe176e70b770c38e7df3d804d2'},
 {'directory': '8c8576394828f016d7981e10199ba7a4dee58cf8',
  'name': 'refs/heads/feature/fix_watch_test_cases_timeout_for_caching_harmony',
  'revision': 'd507632afaa4ec2257601e58e17b455ab2491a58'},
 {'directory': 'b1968bb5bbbd604ef52b10668b04869f5790f7c2',
  'name': 'refs/heads/feature/jsonp-to-push',
  'revision': 'cc26df3dd65062d19fca6268adb866dbf9ec0d8e'},
 {'directory': '2a13a1b4e098680cfc4a3a9a103873a0fce232c4',
  'name': 'refs/heads/feature/postinstall-autolink',
  'revision': '7d4e0b72491819e51e84a8747ebcb07bebcf0f6a'},
 {'directory': '27226447d3a8e6de4dec3878eac3617f922b358c',
  'name': 'refs/heads/feature/travis_yarn_command',
  'revision': 'd370967ac8874214023aa69a22c120d4a0cbdef9'},
 {'directory': '4bd9839b5ade32398ff62a7aced9a32cf89981d0',
  'name': 'refs/heads/feature/webpack_analytics',
  'revision': 'a3461fdc6232bef3e4df3bab5079ab5323df1216'},
 {'directory': '1d427c810ab43e1abfdda73a09af41ea4e314a9f',
  'name': 'refs/heads/feature/webpack_options_apply_coverage_increase',
  'revision': 'b92f3fd3ab21959fcdfe492fb927c70014f16def'},
 {'directory': 'fe6b88dd54f3c1043d32e8af812655ea9b8ba000',
  'name': 'refs/heads/fix/node_modules_mangle',
  'revision': '26f79f5b30ba51afae6219ba53bf52be138c2fd3'},
 {'directory': 'b01142c405b9dba0d73dd8232a310ec469c89379',
  'name': 'refs/heads/inline',
  'revision': '427798d4f0e6b72ca3ecb4bfe849b3a17de08729'},
 {'directory': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'name': 'refs/heads/master',
  'revision': '7bc08e1aa0b08cb23e18715a32aa38517ad34672'},
 {'directory': '63fe66a1ecbb35be33f617f96080a78463f89948',
  'name': 'refs/heads/perf/chunks-set',
  'revision': 'f6f22ef0a733931e217050ad9c3b95265978a556'},
 {'directory': '6b813dd7a42991507ef11bc347d53a28340f563c',
  'name': 'refs/heads/perf/modules-set',
  'revision': 'df44599731b4b1d185b20ccd36e9d37d817ad8c2'},
 {'directory': '29cf488a00126c0e45c78b92f97cdbc733f4d07e',
  'name': 'refs/heads/test/circleci',
  'revision': '0f91f949e2d41ef5cb92493bcc6c1fa7578ac27d'},
 {'directory': 'ea3a49842790b4eb8c3805a3318d8ade15cea6c8',
  'name': 'refs/heads/test/dependency-upgrade',
  'revision': 'c6265492ec886405256e23b9fe4de6dfd1e39c49'},
 {'directory': '4de09be1628ed81def03f78d8d832c93efdf0af4',
  'name': 'refs/heads/test/move-entry',
  'revision': 'a244879a07e04e6b5951520ca3cd80c3ef160f8e'},
 {'directory': '0fa77c20564364056319570bd46607111c97cb42',
  'name': 'refs/heads/webpack-1',
  'revision': 'd4878a55be7a4b7ac4e5db1ae5eef89e15811072'}
]

stub_origin_master_branch = 'HEAD'

stub_origin_root_directory_sha1 = 'ae59ceecf46367e8e4ad800e231fc76adc3afffb'

stub_origin_root_directory_entries = [
 {'checksums': {'sha1': '1a17dd2c8245559b43a90aa7c084572e917effff',
                'sha1_git': '012966bd94e648f23b53e71a3f9918e28abc5d81',
                'sha256': 'd65ab1f8cdb323e2b568a8e99814b1b986a38beed85a380981b383c0feb93525'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 394,
  'name': '.editorconfig',
  'perms': 33188,
  'status': 'visible',
  'target': '012966bd94e648f23b53e71a3f9918e28abc5d81',
  'type': 'file'},
 {'checksums': {'sha1': '2e727ec452dc592ae6038d3e09cd35d83d7ea265',
                'sha1_git': '291a4e25598633cd7c286ad8d6cbe9eee5a6291a',
                'sha256': 'd5951c8b796288e0dae1da50575d1b8619462a8df2272cd250146872a1fe804a'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 1839,
  'name': '.eslintrc.js',
  'perms': 33188,
  'status': 'visible',
  'target': '291a4e25598633cd7c286ad8d6cbe9eee5a6291a',
  'type': 'file'},
 {'checksums': {'sha1': '5c59880c0576b2789ec126b61b09fad7a982763b',
                'sha1_git': 'ac579eb7bc04ba44fe84f3c8d1082573e9f4f514',
                'sha256': '8a59a61ff6c0f568a8f76bab434baf3318c80a75ef6fb1b6eb861a0c97518de0'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 67,
  'name': '.gitattributes',
  'perms': 33188,
  'status': 'visible',
  'target': 'ac579eb7bc04ba44fe84f3c8d1082573e9f4f514',
  'type': 'file'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': '.github',
  'perms': 16384,
  'target': '93bdcf98e9c05307b39a9d9e00e48cda6dbd036c',
  'type': 'dir'},
 {'checksums': {'sha1': '7e1008eee2a373f0db7746d0416856aec6b95c22',
                'sha1_git': '84bc35a3abab38bdf87a8f32cc82ce9c136d331e',
                'sha256': '7de369f1d26bc34c7b6329de78973db07e341320eace6a8704a65d4c5bf5993f'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 167,
  'name': '.gitignore',
  'perms': 33188,
  'status': 'visible',
  'target': '84bc35a3abab38bdf87a8f32cc82ce9c136d331e',
  'type': 'file'},
 {'checksums': {'sha1': '06d96508b7d343ff42868f9b6406864517935da7',
                'sha1_git': '79b049846744a2da3eb1c4ac3b01543f2bdca44a',
                'sha256': '697733061d96dd2e061df04dcd86392bb792e2dbe5725a6cb14a436d3c8b76f1'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 706,
  'name': '.jsbeautifyrc',
  'perms': 33188,
  'status': 'visible',
  'target': '79b049846744a2da3eb1c4ac3b01543f2bdca44a',
  'type': 'file'},
 {'checksums': {'sha1': '8041a4a66f46e615c99a850700850a8bd1079dce',
                'sha1_git': '90e4f1ef5beb167891b2e029da6eb9b14ab17add',
                'sha256': '3d6a76a57351b9e3acc5843ff2127dc2cf70c023133312143f86ee74ba9ef6d3'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 1059,
  'name': '.travis.yml',
  'perms': 33188,
  'status': 'visible',
  'target': '90e4f1ef5beb167891b2e029da6eb9b14ab17add',
  'type': 'file'},
 {'checksums': {'sha1': 'cd52973e43c6f4294e8cdfd3106df602b9993f20',
                'sha1_git': 'e5279ebcecd87445648d003c36e6abfebed0ed73',
                'sha256': '130672b16dff61b1541b6d26c2e568ac11830a31d04faace1583d3ad4a38720e'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 2058,
  'name': 'CONTRIBUTING.md',
  'perms': 33188,
  'status': 'visible',
  'target': 'e5279ebcecd87445648d003c36e6abfebed0ed73',
  'type': 'file'},
 {'checksums': {'sha1': '3bebb9ba92e45dd02a0512e144f6a46b14a9b8ab',
                'sha1_git': '8c11fc7289b75463fe07534fcc8224e333feb7ff',
                'sha256': '9068a8782d2fb4c6e432cfa25334efa56f722822180570802bf86e71b6003b1e'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 1071,
  'name': 'LICENSE',
  'perms': 33188,
  'status': 'visible',
  'target': '8c11fc7289b75463fe07534fcc8224e333feb7ff',
  'type': 'file'},
 {'checksums': {'sha1': '6892825420196e84c7104a7ff71ec75db20a1fca',
                'sha1_git': '8f96a0a6d3bfe7183765938483585f3981151553',
                'sha256': 'b0170cfc28f56ca718b43ab086ca5428f853268687c8c033b4fbf028c66d663e'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 46700,
  'name': 'README.md',
  'perms': 33188,
  'status': 'visible',
  'target': '8f96a0a6d3bfe7183765938483585f3981151553',
  'type': 'file'},
 {'checksums': {'sha1': '9bc4902b282f9f1c9f8f885a6947f3bf0f6e6e5f',
                'sha1_git': 'dd6912c8fc97eff255d64da84cfd9837ebf0a05a',
                'sha256': 'e06dbc101195ec7ea0b9aa236be4bdc03784a01f64d6e11846ce3a3f6e1080c6'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 590,
  'name': 'appveyor.yml',
  'perms': 33188,
  'status': 'visible',
  'target': 'dd6912c8fc97eff255d64da84cfd9837ebf0a05a',
  'type': 'file'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'benchmark',
  'perms': 16384,
  'target': '6bd2996b76e051982aa86499a2b485594e607fe3',
  'type': 'dir'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'bin',
  'perms': 16384,
  'target': '681da97ea1ce9a2bd29e3e72781d80e8b961cd51',
  'type': 'dir'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'buildin',
  'perms': 16384,
  'target': '35cfb25d1b3a4063bf04a43f9cbb7e1e87703708',
  'type': 'dir'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'ci',
  'perms': 16384,
  'target': 'efccd3ce0a0304c8cbcffcfdfcafcf1e598819b8',
  'type': 'dir'},
 {'checksums': {'sha1': '9eb3d0e3711f68f82d29785e64ebff2c0d7cec7a',
                'sha1_git': '1ecf877e445bcf865ef53cfcecadda7e9691aace',
                'sha256': '2007e0883c2784bb82584a10d53a0f0c36286dd913741bfd5e4d22b812db529c'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 529,
  'name': 'circle.yml',
  'perms': 33188,
  'status': 'visible',
  'target': '1ecf877e445bcf865ef53cfcecadda7e9691aace',
  'type': 'file'},
 {'checksums': {'sha1': '63209428718e101492c3bb91509f1b4e319b0d7d',
                'sha1_git': 'b3fa4e6abe22977e6267e9969a593e790bf2cd36',
                'sha256': '5d14c8d70215f46a9722d29c7ebff8cc9bd24509650d7ee601fd461e52a52f7f'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 254,
  'name': 'codecov.yml',
  'perms': 33188,
  'status': 'visible',
  'target': 'b3fa4e6abe22977e6267e9969a593e790bf2cd36',
  'type': 'file'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'examples',
  'perms': 16384,
  'target': '7e3ac01795317fbc36a031a9117e7963d6c7da90',
  'type': 'dir'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'hot',
  'perms': 16384,
  'target': 'a5eea6ca952fba9f7ae4177627ed5e22754df9f5',
  'type': 'dir'},
 {'checksums': {'sha1': '92d9367db4ba049f698f5bf78b6946b8e2d91345',
                'sha1_git': 'eaa9cc4a247b01d6a9c0adc91997fefe6a62be1f',
                'sha256': 'd4b42fa0651cf3d99dea0ca5bd6ba64cc21e80be7d9ea05b2b4423ef8f16ec36'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 19,
  'name': 'input.js',
  'perms': 33188,
  'status': 'visible',
  'target': 'eaa9cc4a247b01d6a9c0adc91997fefe6a62be1f',
  'type': 'file'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'lib',
  'perms': 16384,
  'target': '187d40104aa21475d8af88ccd77fc582cf6ac7a6',
  'type': 'dir'},
 {'checksums': {'sha1': 'f17ffa2dc14262292e2275efa3730a96fe060c44',
                'sha1_git': 'd55b7110929cbba3d94da01494a272b39878ac0f',
                'sha256': '012d4446ef8ab6656251b1b7f8e0217a5666ec04ad952e8a617b70946de17166'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 9132,
  'name': 'open-bot.yaml',
  'perms': 33188,
  'status': 'visible',
  'target': 'd55b7110929cbba3d94da01494a272b39878ac0f',
  'type': 'file'},
 {'checksums': {'sha1': '3a6638e72fcc2499f1a4c9b46d4d00d239bbe1c8',
                'sha1_git': '6d1aa82c90ecd184d136151eb81d240e1fea723e',
                'sha256': '00faf7dde1eb0742f3ca567af4dbcd8c01a38cf30d8faa7f0208f46dbc6b5201'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 4034,
  'name': 'package.json',
  'perms': 33188,
  'status': 'visible',
  'target': '6d1aa82c90ecd184d136151eb81d240e1fea723e',
  'type': 'file'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'schemas',
  'perms': 16384,
  'target': 'f1f89c389f73c29e7a5d1a0ce5f9e0f166857815',
  'type': 'dir'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'test',
  'perms': 16384,
  'target': '318c279189d186a1e06653fc5c78c539878c4d7d',
  'type': 'dir'},
 {'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': None,
  'name': 'web_modules',
  'perms': 16384,
  'target': '93a5cc8e492d0b0323386814a72536381019ef7b',
  'type': 'dir'},
 {'checksums': {'sha1': '8047389fcc8e286ceed5536c677c2e803032cf84',
                'sha1_git': 'eb8509f70158c231a3fd864aecf2649590bbedf3',
                'sha256': '8cbe1ce94349ac3bc6cbcc952efd45d838c6b4524af8a773b18e1ebe8b4f936b'},
  'dir_id': 'ae59ceecf46367e8e4ad800e231fc76adc3afffb',
  'length': 141192,
  'name': 'yarn.lock',
  'perms': 33188,
  'status': 'visible',
  'target': 'eb8509f70158c231a3fd864aecf2649590bbedf3',
  'type': 'file'}
]

stub_origin_sub_directory_path = 'lib/webworker'

stub_origin_sub_directory_entries = [
 {'checksums': {'sha1': '7bf366cd9f4a9835c73aafb70e44f640bab7ad16',
                'sha1_git': '870252b7a175ee5ec2edfe2c22b2d56aa04bece4',
                'sha256': 'e0af438932627dd9d53b36bfe69c3dbad6dc4d4569f6cdb29d606c9df2b128fa'},
  'dir_id': '02b626051e0935ecd28f50337f452db76803f980',
  'length': 921,
  'name': 'WebWorkerChunkTemplatePlugin.js',
  'perms': 33188,
  'status': 'visible',
  'target': '870252b7a175ee5ec2edfe2c22b2d56aa04bece4',
  'type': 'file'},
 {'checksums': {'sha1': 'e2862b2787702bd3eb856f73627d5d8df5a8b550',
                'sha1_git': 'b3e90d26a68ad9da0a7cc97a262db585fa4c73ba',
                'sha256': '1c254e76248ff5ec7e2185cdb1cfd2e0338087244d2d617a868c346317b7646b'},
  'dir_id': '02b626051e0935ecd28f50337f452db76803f980',
  'length': 1039,
  'name': 'WebWorkerHotUpdateChunkTemplatePlugin.js',
  'perms': 33188,
  'status': 'visible',
  'target': 'b3e90d26a68ad9da0a7cc97a262db585fa4c73ba',
  'type': 'file'},
 {'checksums': {'sha1': 'a1e04061d3e50bb8c024b07e9464da7392f37bf1',
                'sha1_git': '1e503e028fdd5322c9f7d8ec50f54006cacf334e',
                'sha256': '72dea06510d1a4435346f8dca20d8898a394c52c7382a97bd73d1840e31f90b3'},
  'dir_id': '02b626051e0935ecd28f50337f452db76803f980',
  'length': 1888,
  'name': 'WebWorkerMainTemplate.runtime.js',
  'perms': 33188,
  'status': 'visible',
  'target': '1e503e028fdd5322c9f7d8ec50f54006cacf334e',
  'type': 'file'},
 {'checksums': {'sha1': 'b95c16e90784cf7025352839133b482149526da0',
                'sha1_git': '46c9fe382d606ce19e556deeae6a23af47a8027d',
                'sha256': 'c78c7ca9ee0aa341f843a431ef27c75c386607be3037d44ff530bfe3218edb3c'},
  'dir_id': '02b626051e0935ecd28f50337f452db76803f980',
  'length': 4051,
  'name': 'WebWorkerMainTemplatePlugin.js',
  'perms': 33188,
  'status': 'visible',
  'target': '46c9fe382d606ce19e556deeae6a23af47a8027d',
  'type': 'file'},
 {'checksums': {'sha1': 'ec9df36b1e8dd689d84dbeeeb9f45fe9f9d96605',
                'sha1_git': 'd850018bb0d2ad41dd0ae9e5c887dff8a23601e9',
                'sha256': 'f995f6a13511955244850c2344c6cef09c10ab24c49f8448544e2b34aa69d03c'},
  'dir_id': '02b626051e0935ecd28f50337f452db76803f980',
  'length': 763,
  'name': 'WebWorkerTemplatePlugin.js',
  'perms': 33188,
  'status': 'visible',
  'target': 'd850018bb0d2ad41dd0ae9e5c887dff8a23601e9',
  'type': 'file'}
]

stub_content_origin_info = {
    'id': 10357753,
    'type': 'git',
    'url': 'https://github.com/KDE/kate'
}

stub_content_origin_visit_id = 10
stub_content_origin_visit_unix_ts = 1494032350
stub_content_origin_visit_iso_date = '2017-05-06T00:59:10+00:00'

stub_content_origin_branch = 'HEAD'

stub_content_origin_visits = [
 {'date': '2015-09-26T09:30:52.373449+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 1},
 {'date': '2016-03-10T05:36:11.118989+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 2},
 {'date': '2016-03-24T07:39:29.727793+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 3},
 {'date': '2016-03-31T22:55:31.402863+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 4},
 {'date': '2016-05-26T06:25:54.879676+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 5},
 {'date': '2016-06-07T17:16:33.964164+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 6},
 {'date': '2016-07-27T01:38:20.345358+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 7},
 {'date': '2016-08-13T04:46:45.987508+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 8},
 {'date': '2016-08-16T23:24:13.214496+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 9},
 {'date': '2016-08-17T18:10:39.841005+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 10},
 {'date': '2016-08-30T17:28:02.476486+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 11},
 {'date': '2016-09-08T09:32:37.152054+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 12},
 {'date': '2016-09-15T09:47:37.758093+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 13},
 {'date': '2016-12-04T06:14:02.688518+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 14},
 {'date': '2017-02-16T08:45:57.719974+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'partial',
  'visit': 15},
 {'date': '2017-05-06T00:59:10.495727+00:00',
  'metadata': {},
  'origin': 10357753,
  'status': 'full',
  'visit': 16}
]

stub_content_origin_branches = [
 {'directory': '08e8329257dad3a3ef7adea48aa6e576cd82de5b',
  'name': 'HEAD',
  'revision': '11f15b0789344427ddf17b8d75f38577c4395ce0'},
 {'directory': '2371baf0411e3adf12d65daf86c3b135633dd5e4',
  'name': 'refs/heads/Applications/14.12',
  'revision': '5b27ad32f8c8da9b6fc898186d59079488fb74c9'},
 {'directory': '5d024d33a218eeb164936301a2f89231d1f0854a',
  'name': 'refs/heads/Applications/15.04',
  'revision': '4f1e29120795ac643044991e91f24d02c9980202'},
 {'directory': 'f33984df50ec29dbbc86295adb81ebb831e3b86d',
  'name': 'refs/heads/Applications/15.08',
  'revision': '52722e588f46a32b480b5f304ba21480fc8234b1'},
 {'directory': 'e706b836cf32929a48b6f92c07766f237f9d068f',
  'name': 'refs/heads/Applications/15.12',
  'revision': '38c4e42c4a653453fc668c704bb8995ae31b5baf'},
 {'directory': 'ebf8ae783b44df5c827bfa46227e5dbe98f25eb4',
  'name': 'refs/heads/Applications/16.04',
  'revision': 'd0fce3b880ab37a551d75ec940137e0f46bf2143'},
 {'directory': '68ea0543fa80cc512d969fc2294d391a904e04fa',
  'name': 'refs/heads/Applications/16.08',
  'revision': '0b05000bfdde06aec2dc6528411ec24c9e20e672'},
 {'directory': 'b9481c652d57b2e0e36c63f2bf795bc6ffa0b6a1',
  'name': 'refs/heads/Applications/16.12',
  'revision': '2a52ca09fce28e29f5afd0ba4622635679036837'},
 {'directory': '415ea4716870c59feabde3210da6f60bcf897479',
  'name': 'refs/heads/Applications/17.04',
  'revision': 'c7ba6cef1ebfdb743e4f3f53f51f44917981524a'},
 {'directory': 'a9d27a5cd354f2f1e50304ef72818141231f7876',
  'name': 'refs/heads/KDE/4.10',
  'revision': 'e0bc3d8ab537d06c817c459f0be7c7f21d670b6e'},
 {'directory': 'a273331f42e6998099ac98934f33431eb244b222',
  'name': 'refs/heads/KDE/4.11',
  'revision': 'e9db108b584aabe88eff1969f408146b0b9eac32'},
 {'directory': '00be5902593157c55a9888b9e5c17c3b416d1f89',
  'name': 'refs/heads/KDE/4.12',
  'revision': 'c2a1c24f28613342985aa40573fb922370900a3a'},
 {'directory': 'f25aa509cc4ad99478a71407850575d267ae4106',
  'name': 'refs/heads/KDE/4.13',
  'revision': 'b739b7a67882408b4378d901c38b2c88108f1312'},
 {'directory': 'e39f1a6967c33635c9e0c3ee627fbd987612417b',
  'name': 'refs/heads/KDE/4.14',
  'revision': 'dd6530d110b165dfeed8dc1b20b8cfab0e4bd25b'},
 {'directory': '5ac8842a402fe3136be5e2ddd31cb24232152994',
  'name': 'refs/heads/KDE/4.7',
  'revision': '776b581f5f724b1179f2fe013c2da835bb0d5cfc'},
 {'directory': '1e6d88a64ecfa70a6883efd977bfd6248344b108',
  'name': 'refs/heads/KDE/4.8',
  'revision': 'fe3723f6ab789ecf21864e198c91092d10a5289b'},
 {'directory': 'aa03927b4d5738c67646509b4b5d55faef03f024',
  'name': 'refs/heads/KDE/4.9',
  'revision': '69121e434e25f8f4c8ee92a1771a8e87913b3559'},
 {'directory': '57844f10b9ade482ece88ae07a406570e5c0b35d',
  'name': 'refs/heads/goinnn-kate-plugins',
  'revision': 'f51e7810338fe5648319a88712d0ce560cc5f847'},
 {'directory': 'eed636cada058599df292eb59180896cd8aeceac',
  'name': 'refs/heads/kfunk/fix-katecompletionmodel',
  'revision': 'dbf7cae67c5db0737fcf37235000b867cd839f3e'},
 {'directory': '08e8329257dad3a3ef7adea48aa6e576cd82de5b',
  'name': 'refs/heads/master',
  'revision': '11f15b0789344427ddf17b8d75f38577c4395ce0'},
 {'directory': '7b5bdcb46cfaa25229af6b038190b004a26397ff',
  'name': 'refs/heads/plasma/sreich/declarative-kate-applet',
  'revision': '51ab3ea145abd3219c3fae06ff99fa911a6a8993'},
 {'directory': 'e39f1a6967c33635c9e0c3ee627fbd987612417b',
  'name': 'refs/pull/1/head',
  'revision': 'dd6530d110b165dfeed8dc1b20b8cfab0e4bd25b'}
]