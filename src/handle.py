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

def handle_ret(fn):
    data = []
    with open(fn, 'r') as tin:
        traj = tin.readlines()
        i = 0;
        for line in traj:
            traj_dic = {
                    'geometry':{
                        'type': 'Point',
                        'coordinates':[]
                        }
                    }

            line = line.strip().split(' ')
            line = [float(x) for x in line]
            traj_dic['geometry']['coordinates'].append(line[1])
            traj_dic['geometry']['coordinates'].append(line[2])
            traj_dic['time'] = i 
            i += 1
            data.append(traj_dic)
    json.dump(data, open('ret.js', 'w'))

if __name__ == '__main__':
    # handle('traj_gps.txt')
    handle_ret('result.txt')

