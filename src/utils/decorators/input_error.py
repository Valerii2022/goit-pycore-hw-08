from colorama import Fore, Style

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return Fore.RED + "Contact not found. Please provide a valid name." + Style.RESET_ALL
        except IndexError:
            return Fore.RED +  "Please provide the correct number of arguments." + Style.RESET_ALL
        except ValueError as e:
            return Fore.RED +  f"Give me correct name and phone please. {e}" + Style.RESET_ALL
        except Exception:
            return Fore.RED +  "An unexpected error occurred. Please try again." + Style.RESET_ALL
    return wrapper

