from burp import IBurpExtender
from burp import IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("URL Extractor")
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest:
            url = self._helpers.analyzeRequest(messageInfo).getUrl()
            with open("file.txt", "a") as f:
                f.write(url.toString() + "\n")

extender = BurpExtender()