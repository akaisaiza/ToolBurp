import check_validity 
import proxyburp
logo = """            __  __  __  __  __  __                     
           / /_  __  ___________  ____ _
          / __ \/ / / / ___/ __ \/ __ `/
         / /_/ / /_/ / /  / /_/ / /_/ / 
        /_.___/\__,_/_/  / .___/  
                        /_/             
         hacker is chickens 
"""
def input_url():
    url = input("Target URL: ")
    if check_validity.validate_url(url):
        return url
    else:
        print("URL không hợp lệ.")
if __name__ == "__main__":
    print(logo)
    proxyburp.proxy_config(input_url())