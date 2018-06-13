import json
import random

k = 100

def handle(fn):
    with open(fn, 'r') as tin:
        trajs = tin.readlines()
        traj_1000 = random.sample(trajs, k)
        data = []
        for line in traj_1000:
            traj_dic = {}
            geometry = {'type': 'LineString', 'coordinates':[]}
    
            traj = line.strip().split('\t')
            sample_num = int(traj[1])
            for i in range(2, sample_num*3+2, 3):
                geometry['coordinates'].append([float(traj[i+1]),float(traj[i+2])])
            traj_dic['geometry'] = geometry
            data.append(traj_dic)
        json.dump(data, open('traj_100.js', 'w'))


if __name__ == '__main__':
    handle('traj_gps.txt')
