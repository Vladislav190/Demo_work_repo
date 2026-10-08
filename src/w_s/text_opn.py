import json
def js_open(t: str):
    with open(t, "r") as ff:
        file = (json.load(ff))
        param = file['chain']
    return param

def txt_open(js: str):
    with open(js, "r") as fa:
        #np.load(files_txt)
        text_input = fa.read()
        rows = text_input.split('\n')
        u_t = []
        for i in rows:
            if len(i) == 0:
                continue
            el = i.split(' ')
            u_t.append([float(o) for o in el]) 
    return u_t