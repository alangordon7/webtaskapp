FILEPATH = "WAtasklist.txt"

def get_task_list(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        task_list_local = file_local.readlines()
    return task_list_local


def write_task_list(task_list_argument, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(task_list_argument)
