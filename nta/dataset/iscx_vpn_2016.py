import pandas as pd


a = '''
.
├── NonVPN-PCAPs
│   ├── AIMchat1.pcapng
│   ├── AIMchat2.pcapng
│   ├── ICQchat1.pcapng
│   ├── ICQchat2.pcapng
│   ├── aim_chat_3a.pcap
│   ├── aim_chat_3b.pcap
│   ├── email1a.pcap
│   ├── email1b.pcap
│   ├── email2a.pcap
│   ├── email2b.pcap
│   ├── facebook_audio1a.pcap
│   ├── facebook_audio1b.pcapng
│   ├── facebook_audio2a.pcap
│   ├── facebook_audio2b.pcapng
│   ├── facebook_audio3.pcapng
│   ├── facebook_audio4.pcapng
│   ├── facebook_chat_4a.pcap
│   ├── facebook_chat_4b.pcap
│   ├── facebook_video1a.pcap
│   ├── facebook_video1b.pcapng
│   ├── facebook_video2a.pcap
│   ├── facebook_video2b.pcapng
│   ├── facebookchat1.pcapng
│   ├── facebookchat2.pcapng
│   ├── facebookchat3.pcapng
│   ├── ftps_down_1a.pcap
│   ├── ftps_down_1b.pcap
│   ├── ftps_up_2a.pcap
│   ├── ftps_up_2b.pcap
│   ├── gmailchat1.pcapng
│   ├── gmailchat2.pcapng
│   ├── gmailchat3.pcapng
│   ├── hangout_chat_4b.pcap
│   ├── hangouts_audio1a.pcap
│   ├── hangouts_audio1b.pcapng
│   ├── hangouts_audio2a.pcap
│   ├── hangouts_audio2b.pcapng
│   ├── hangouts_audio3.pcapng
│   ├── hangouts_audio4.pcapng
│   ├── hangouts_chat_4a.pcap
│   ├── hangouts_video1b.pcapng
│   ├── hangouts_video2a.pcap
│   ├── hangouts_video2b.pcapng
│   ├── icq_chat_3a.pcap
│   ├── icq_chat_3b.pcap
│   ├── netflix1.pcap
│   ├── netflix2.pcap
│   ├── netflix3.pcap
│   ├── netflix4.pcap
│   ├── scp1.pcapng
│   ├── scpDown1.pcap
│   ├── scpDown2.pcap
│   ├── scpDown3.pcap
│   ├── scpDown4.pcap
│   ├── scpDown5.pcap
│   ├── scpDown6.pcap
│   ├── scpUp1.pcap
│   ├── scpUp2.pcap
│   ├── scpUp3.pcap
│   ├── scpUp5.pcap
│   ├── scpUp6.pcap
│   ├── sftp1.pcapng
│   ├── sftpDown1.pcap
│   ├── sftpDown2.pcap
│   ├── sftpUp1.pcap
│   ├── sftp_down_3a.pcap
│   ├── sftp_down_3b.pcap
│   ├── sftp_up_2a.pcap
│   ├── sftp_up_2b.pcap
│   ├── skype_audio1a.pcap
│   ├── skype_audio1b.pcapng
│   ├── skype_audio2a.pcap
│   ├── skype_audio2b.pcapng
│   ├── skype_audio3.pcapng
│   ├── skype_audio4.pcapng
│   ├── skype_chat1a.pcap
│   ├── skype_chat1b.pcap
│   ├── skype_file1.pcap
│   ├── skype_file2.pcap
│   ├── skype_file3.pcap
│   ├── skype_file4.pcapng
│   ├── skype_file5.pcapng
│   ├── skype_file6.pcapng
│   ├── skype_file7.pcapng
│   ├── skype_file8.pcapng
│   ├── skype_video1a.pcap
│   ├── skype_video1b.pcapng
│   ├── skype_video2a.pcap
│   ├── skype_video2b.pcapng
│   ├── spotify1.pcap
│   ├── spotify2.pcap
│   ├── spotify3.pcap
│   ├── spotify4.pcap
│   ├── vimeo1.pcap
│   ├── vimeo2.pcap
│   ├── vimeo3.pcap
│   ├── vimeo4.pcap
│   ├── voipbuster1b.pcapng
│   ├── voipbuster2b.pcapng
│   ├── voipbuster3b.pcapng
│   ├── voipbuster_4a.pcap
│   ├── voipbuster_4b.pcap
│   ├── youtube1.pcap
│   ├── youtube2.pcap
│   ├── youtube3.pcap
│   ├── youtube4.pcap
│   ├── youtube5.pcap
│   ├── youtube6.pcap
│   └── youtubeHTML5_1.pcap
└── VPN-PCAPS
    ├── vpn_aim_chat1a.pcap
    ├── vpn_aim_chat1b.pcap
    ├── vpn_bittorrent.pcap
    ├── vpn_email2a.pcap
    ├── vpn_email2b.pcap
    ├── vpn_facebook_audio2.pcap
    ├── vpn_facebook_chat1a.pcap
    ├── vpn_facebook_chat1b.pcap
    ├── vpn_ftps_A.pcap
    ├── vpn_ftps_B.pcap
    ├── vpn_hangouts_audio1.pcap
    ├── vpn_hangouts_audio2.pcap
    ├── vpn_hangouts_chat1a.pcap
    ├── vpn_hangouts_chat1b.pcap
    ├── vpn_icq_chat1a.pcap
    ├── vpn_icq_chat1b.pcap
    ├── vpn_netflix_A.pcap
    ├── vpn_sftp_A.pcap
    ├── vpn_sftp_B.pcap
    ├── vpn_skype_audio1.pcap
    ├── vpn_skype_audio2.pcap
    ├── vpn_skype_chat1a.pcap
    ├── vpn_skype_chat1b.pcap
    ├── vpn_skype_files1a.pcap
    ├── vpn_skype_files1b.pcap
    ├── vpn_spotify_A.pcap
    ├── vpn_vimeo_A.pcap
    ├── vpn_vimeo_B.pcap
    ├── vpn_voipbuster1a.pcap
    ├── vpn_voipbuster1b.pcap
    └── vpn_youtube_A.pcap
'''

class ISCX_VPN_2016():

    def __init__(self, cap_dir, ) -> None:
        pass

    
    def get_label_by_task(self, task_name):
        assert task_name in ['VPN-nonVPN', 'VPN', 'NonVPN', 'Categories']


    def file2label(self, class_task='vpn-nonvpn'):
        # 排除在外的 pcap
        exclude_list = []
        task_vpn_nonvpn = ['VPN', 'NonVPN']
        task_categories = ['VPN_Chat', 'VPN_Email', 'VPN_FileTransfer', 'VPN_P2P', 'VPN_Streaming', 'VPN_VoIP', 'Chat', 'Email', 'FileTransfer', 'P2P', 'Streaming', 'VoIP']

        [{'file_name': 'AIMchat1.pcapng', 'label_2': 'VPN_Chat'}]

        return {

        }
