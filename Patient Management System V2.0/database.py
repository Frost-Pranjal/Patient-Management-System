from pymongo import MongoClient
import datetime

cluster = MongoClient("mongodb+srv://wellnessManagement:CWP0YyKCPPwYjXLL@cluster0.610owjf.mongodb.net/?retryWrites=true&w=majority")
db = cluster["patient_user"]
db1 = cluster["hospital_user"]
db2 = cluster["adminDB"]

def pDetails():

    collection = db["patient_details"]
    i = collection.count_documents({})

    return(i+1)


def pFullDetails(uid):
    collection = db["patient_details"]

    data = collection.find_one({"_id": uid}, {'_id':1, 'name': 1, 'dob':1, 'phoneNumber':1, 'address':1, 'email':1})

    return data

def getMedRec(uid):
    collection = db["patient-medical_history"]
    data = collection.find_one({"uid": uid}, {'_id':0, 'record': 1})

    return data['record']

def authDetails():

    collection = db["patient_authentication"]
    i = collection.count_documents({})

    if i == 0:
        return []

    cursor = collection.find({}, {'_id':0, 'username': 1})
    u = []
    for user in cursor:
        u.append(user['username'])

    return u

def getPass(uid):

    collection = db["patient_authentication"]
    
    p = collection.find_one({"username": uid}, {'_id':0, 'password': 1}) ['password']

    return p

def insertAuth(data):
    collection = db["patient_authentication"]
    collection.insert_one(data)

def insertProf(data):
    collection = db["patient_details"]
    collection.insert_one(data)

def insertRec(data):
    collection = db["patient-medical_history"]
    collection.insert_one(data)


def getUidUser(user):
    collection = db["patient_authentication"]
    
    ui = collection.find_one({"username": user}, {'_id':0, 'uid': 1}) ['uid']

    return ui


def updateProfile(uid, n, d, p, a, e):
    collection = db["patient_details"]

    mQuery = {"_id":uid}

    newN = {"$set" : {"name":n}}
    newd = {"$set" : {"dob": d}}
    newp = {"$set" : {"phoneNumber":p}}
    newa = {"$set" : {"address":a}}
    newe = {"$set" : {"email":e}}

    collection.update_one(mQuery, newN)
    collection.update_one(mQuery, newd)
    collection.update_one(mQuery, newp)
    collection.update_one(mQuery, newa)
    collection.update_one(mQuery, newe)

def updateMedHistory(uid, t):
    collection = db["patient-medical_history"]

    mQuery = {"uid": uid}

    newM = {"$set": {"record": t}}

    collection.update_one(mQuery, newM)

def changeP(uid, p):
    collection = db["patient_authentication"]

    mQuery = {"username": uid}

    newM = {"$set": {"password": p}}

    collection.update_one(mQuery, newM)

def getHospConIds(uid):
    collection = db["hospital_record"]
    data = collection.find_one({"uid": uid}, {'_id':0, 'hospitals': 1}) 

    if data == None:
        return ''

    data = data['hospitals']
    for keys, values in data.items():
        if "ongoing" in values.values():
            return keys

    return ''

def getHospitalInfo(hid):
    collection = db1["hospital_detail"]
    data = collection.find_one({"_id": int(hid)}, {})
 
    return data


def getHospHist(uid):
    collection = db["hospital_record"]
    data = collection.find_one({"uid": uid}, {'_id':0, 'hospitals': 1})
    if data == None:
        return []
        
    data = data ['hospitals']
    res=[]
    for keys, values in data.items():
        if "ongoing" in values.values():
            continue
        res.append([keys, values["starting"], values["status"]])
    
    return res

def getHosAuth():
    collection = db1["hospital_authentication"]
    i = collection.count_documents({})

    if i == 0:
        return []

    cursor = collection.find({}, {'_id':0, 'username': 1})
    u = []
    for user in cursor:
        u.append(user['username'])

    return u

def getHpass(user):
    collection = db1["hospital_authentication"]
    p = collection.find_one({"username": user}, {'_id':0, 'password': 1}) ['password']

    return p

def getHospId(user):
    collection = db1["hospital_authentication"]
    hid = collection.find_one({"username": user}, {'_id':0, 'hid': 1}) ['hid']

    return hid
    

def updateHosp(hid, n, a, p):
    collection = db1["hospital_detail"]

    mQuery = {"_id":hid}

    newN = {"$set" : {"name":n}}
    newp = {"$set" : {"phone":p}}
    newa = {"$set" : {"address":a}}

    collection.update_one(mQuery, newN)
    collection.update_one(mQuery, newp)
    collection.update_one(mQuery, newa)

def changeHpass(user, p):
    collection = db1["hospital_authentication"]
    mQuery = {"username": user}

    newM = {"$set": {"password": p}}

    collection.update_one(mQuery, newM)


def patForHosp(hid):
    uids=[]
    collection = db["hospital_record"]
    data = collection.find({})
    for doc in data:
        for hids in doc['hospitals'].items():
            if int(hids[0]) == hid:
                status = hids[1]['status']
                if status == 'ongoing':

                    uids.append([doc['uid'], hids[1]['starting']])

    return uids


def changeOngoing(uid):
    now = datetime.datetime.now().year
    collection = db["hospital_record"]
    data = collection.find_one({'uid': uid}, {'hospitals': 1, '_id':0})
    print(data)
    if data == None:
        print(7)
    else:
        data = collection.find_one({'uid': uid}, {'hospitals': 1, '_id':0})['hospitals']
        for v in data.values():
            if v['status'] == 'ongoing':
                v['status'] = str(now)


        mQuery = {"uid": uid}
        newR = {"$set": {"hospitals": data}}

        collection.update_one(mQuery, newR)

def addHosp(hid, uid):
    now = datetime.datetime.now().year
    collection = db["hospital_record"]
    data = collection.find_one({'uid': uid}, {'hospitals': 1, '_id':0})

    if data == None:
        ins = {'uid':uid, 'hospitals':{hid:{'starting':now, 'status':'ongoing'}}}
        collection.insert_one(ins)
    else:
        data = collection.find_one({'uid': uid}, {'hospitals': 1, '_id':0})['hospitals']

        newD = {"starting": now, "status": "ongoing"}

        data[str(hid)] = newD


        mQuery = {"uid": uid}
        newR = {"$set": {"hospitals": data}}

        collection.update_one(mQuery, newR)

def adminAuth():
    collection = db2["admin_auth"]

    i = collection.count_documents({})

    if i == 0:
        return []

    cursor = collection.find({}, {'_id':0, 'user': 1})
    u = []
    for user in cursor:
        u.append(user['user'])

    return u


def adminPass(user):
    collection = db2["admin_auth"]

    p = collection.find_one({"user": user}, {"_id":0, "password": 1})['password']

    return p


def changeApass(user, p):
    collection = db2["admin_auth"]
    mQuery = {"user": user}

    newM = {"$set": {"password": p}}

    collection.update_one(mQuery, newM)

def getHospDet():
    collection = db1["hospital_detail"]
    data = collection.find({}, {})
    retData = []
    for doc in data:
        retData.append(doc)
    return retData

def insertHos(data):
    collection = db1["hospital_detail"]
    collection.insert_one(data)

def insertHopAuth(data):
    collection = db1["hospital_authentication"]
    collection.insert_one(data)
