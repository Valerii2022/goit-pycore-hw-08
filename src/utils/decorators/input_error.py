def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found. Please provide a valid name."
        except ValueError as e:
            return f"Give me correct name and phone please. {e}"
        except IndexError:
            return "Please provide the correct number of arguments."
        except Exception:
            return "An unexpected error occurred. Please try again."
    return wrapper