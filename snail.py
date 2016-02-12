import weechat
end_command = ">> /var/log/highlight.log"
import subprocess
weechat.register("snail", "Bsdpunk", "1.0", "GPL3", "Test script", "", "")
weechat.prnt("", "Hello, from python script!")
import requests
key = "mailgun_api_key"
sandbox = "mailgun_domain"
recipient = 'my_number@sms-gateway.carrier.com'

def join_cb(data, signal, signal_data):
    nick = weechat.info_get("irc_nick_from_host", signal_data)
    server = signal.split(",")[0]
    channel = signal_data.split(":")[-1]
    buffer = weechat.info_get("irc_buffer", "%s,%s" % (server, channel))
    if buffer:
        weechat.prnt(buffer, "Eheh, %s has joined this channel!" % nick)
    return weechat.WEECHAT_RC_OK

def message(data, bufferp, uber_empty, tagsn, isdisplayed, ishilight, prefix, message):
    #weechat.prnt("", data)
    #weechat.prnt("", bufferp)
    #weechat.prnt("", uber_empty)
    #weechat.prnt("", tagsn)
    #weechat.prnt("", isdisplayed)
    #weechat.prnt("", ishilight)
    #weechat.prnt("", prefix)
    #weechat.prnt("", message)
    if int(ishilight):
    weechat.prnt("", message)
        full_command = "echo '" +message + "' " + end_command
        weechat.prnt("", full_command)
        process = subprocess.call(full_command, shell=True)
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
        request = requests.post(request_url, auth=('api', key), data={
            'from': 'hammer@mechanicalpinata.com',
            'to': recipient,
            'subject': "IRC Message",
            'text':prefix+' '+message
        })
        weechat.prnt('','Status: {0}'.format(request.status_code))
        weechat.prnt('','Body:   {0}'.format(request.text))
    return weechat.WEECHAT_RC_OK

weechat.hook_print("", "irc_privmsg", "", 1, "message", "")import weechat
end_command = ">> /var/log/highlight.log"
import subprocess
weechat.register("snail", "Bsdpunk", "1.0", "GPL3", "Test script", "", "")
weechat.prnt("", "Hello, from python script!")
import requests
key = "mailgun_api_key"
sandbox = "mailgun_domain"
recipient = 'my_number@sms-gateway.carrier.com'

def join_cb(data, signal, signal_data):
    nick = weechat.info_get("irc_nick_from_host", signal_data)
    server = signal.split(",")[0]
    channel = signal_data.split(":")[-1]
    buffer = weechat.info_get("irc_buffer", "%s,%s" % (server, channel))
    if buffer:
        weechat.prnt(buffer, "Eheh, %s has joined this channel!" % nick)
    return weechat.WEECHAT_RC_OK

def message(data, bufferp, uber_empty, tagsn, isdisplayed, ishilight, prefix, message):
    #weechat.prnt("", data)
    #weechat.prnt("", bufferp)
    #weechat.prnt("", uber_empty)
    #weechat.prnt("", tagsn)
    #weechat.prnt("", isdisplayed)
    #weechat.prnt("", ishilight)
    #weechat.prnt("", prefix)
    #weechat.prnt("", message)
    if int(ishilight):
    weechat.prnt("", message)
        full_command = "echo '" +message + "' " + end_command
        weechat.prnt("", full_command)
        process = subprocess.call(full_command, shell=True)
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
        request = requests.post(request_url, auth=('api', key), data={
            'from': 'hammer@mechanicalpinata.com',
            'to': recipient,
            'subject': "IRC Message",
            'text':prefix+' '+message
        })
        weechat.prnt('','Status: {0}'.format(request.status_code))
        weechat.prnt('','Body:   {0}'.format(request.text))
    return weechat.WEECHAT_RC_OK

weechat.hook_print("", "irc_privmsg", "", 1, "message", "")
