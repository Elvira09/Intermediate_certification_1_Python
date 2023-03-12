import ui.view as v
import util.data_write as w
import util.config as c
import service.service as s


path = c.path

def button_click():
    action = v.get_action()

    if action == 1:
        w.write_data(path)
    elif action == 2:
        s.search_note()
    elif action == 3:
        w.write_edit_data(path)
    elif action == 4:
        w.write_del_data(path)
    elif action == 5:
        s.show_notes()
