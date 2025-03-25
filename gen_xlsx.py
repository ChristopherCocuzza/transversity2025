#!/usr/bin/env python
import sys,os,time
import numpy as np
import scipy
import copy

import pandas as pd

import lhapdf

if __name__=="__main__":

    X = np.linspace(0.001,0.99,1000)
    Q2 = 4*np.ones(len(X))
    flavs = ['uv','dv']

    data = {}
    data['X']  = X
    data['Q2'] = Q2

    os.environ['LHAPDF_DATA_PATH'] = '.'#'%s/qcdlib/lhapdf'%(os.environ['FITPACK'])
    #--get JAM3D with LQCD
    QCF = lhapdf.mkPDFs('JAM23-transversity_proton_lo')
    nrep = len(QCF)

    store = {flav: [] for flav in flavs} 
    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        dv =  np.array([QCF[i].xfxQ2( 1,x,Q2[0])-QCF[i].xfxQ2(-1,x,Q2[0]) for x in X])
        uv =  np.array([QCF[i].xfxQ2( 2,x,Q2[0])-QCF[i].xfxQ2(-2,x,Q2[0]) for x in X])
        store['dv'].append(dv)
        store['uv'].append(uv)

    data['uv_mean_JAM3D*_w/LQCD'] = np.mean(store['uv'],axis=0)
    data['uv_std_JAM3D*_w/LQCD']  = np.std (store['uv'],axis=0)
    data['dv_mean_JAM3D*_w/LQCD'] = np.mean(store['dv'],axis=0)
    data['dv_std_JAM3D*_w/LQCD']  = np.std (store['dv'],axis=0)
   

    #--get JAM3D without LQCD
    QCF = lhapdf.mkPDFs('JAM23-transversity_proton_lo_nolat')
    nrep = len(QCF)

    store = {flav: [] for flav in flavs} 
    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        dv =  np.array([QCF[i].xfxQ2( 1,x,Q2[0])-QCF[i].xfxQ2(-1,x,Q2[0]) for x in X])
        uv =  np.array([QCF[i].xfxQ2( 2,x,Q2[0])-QCF[i].xfxQ2(-2,x,Q2[0]) for x in X])
        store['dv'].append(dv)
        store['uv'].append(uv)

    data['uv_mean_JAM3D*_noLQCD'] = np.mean(store['uv'],axis=0)
    data['uv_std_JAM3D*_noLQCD']  = np.std (store['uv'],axis=0)
    data['dv_mean_JAM3D*_noLQCD'] = np.mean(store['dv'],axis=0)
    data['dv_std_JAM3D*_noLQCD']  = np.std (store['dv'],axis=0)


    #--get JAMDiFF with LQCD
    QCF = lhapdf.mkPDFs('JAMDiFF23-transversity_lo')
    nrep = len(QCF)

    store = {flav: [] for flav in flavs} 
    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        dv =  np.array([QCF[i].xfxQ2( 1,x,Q2[0])-QCF[i].xfxQ2(-1,x,Q2[0]) for x in X])
        uv =  np.array([QCF[i].xfxQ2( 2,x,Q2[0])-QCF[i].xfxQ2(-2,x,Q2[0]) for x in X])
        store['dv'].append(dv)
        store['uv'].append(uv)

    data['uv_mean_JAMDiFF*_w/LQCD'] = np.mean(store['uv'],axis=0)
    data['uv_std_JAMDiFF*_w/LQCD']  = np.std (store['uv'],axis=0)
    data['dv_mean_JAMDiFF*_w/LQCD'] = np.mean(store['dv'],axis=0)
    data['dv_std_JAMDiFF*_w/LQCD']  = np.std (store['dv'],axis=0)


    #--get JAMDiFF without LQCD
    QCF = lhapdf.mkPDFs('JAMDiFF23-transversity_lo_nolat')
    nrep = len(QCF)

    store = {flav: [] for flav in flavs} 
    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        dv =  np.array([QCF[i].xfxQ2( 1,x,Q2[0])-QCF[i].xfxQ2(-1,x,Q2[0]) for x in X])
        uv =  np.array([QCF[i].xfxQ2( 2,x,Q2[0])-QCF[i].xfxQ2(-2,x,Q2[0]) for x in X])
        store['dv'].append(dv)
        store['uv'].append(uv)

    data['uv_mean_JAMDiFF_noLQCD'] = np.mean(store['uv'],axis=0)
    data['uv_std_JAMDiFF_noLQCD']  = np.std (store['uv'],axis=0)
    data['dv_mean_JAMDiFF_noLQCD'] = np.mean(store['dv'],axis=0)
    data['dv_std_JAMDiFF_noLQCD']  = np.std (store['dv'],axis=0)





    data = pd.DataFrame(data)
    data.to_excel('text.xlsx',index=False)
 
    

