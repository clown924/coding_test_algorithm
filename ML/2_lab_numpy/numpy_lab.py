import numpy as np

def n_size_ndarray_creation(n, dtype=np.int8):
    # return np.array(range(n**2),dtype = dtype).reshape(n,n)
    return np.arange(n**2).reshape(n,n)

n = 3
print(n_size_ndarray_creation(n))

def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int8):
    if type == 0:
        return np.zeros(shape=shape,dtype=dtype)
    if type == 1:
        return np.ones(shape=shape,dtype=dtype)
    if type == 99:
        return np.empty(shape=shape,dtype=dtype)

print(zero_or_one_or_empty_ndarray((3,3),99))


def change_shape_of_ndarray(X, n_row):
    return X.flatten() if n_row==1 else X.reshape(n_row,-1)

X = np.ones((32,32),dtype=np.int8)
change_shape_of_ndarray(X,512)


def concat_ndarray(X_1, X_2, axis):
    try:
        if X_1.ndim == 1:  # 벡터면
            X_1 = X_1.reshape(1,-1)
        if X_2.ndim == 1:
            X_2 = X_2.reshape(1,-1)
        return np.concatenate((X_1,X_2),axis = axis)
    except ValueError as e:
        return False

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
concat_ndarray(a,b,1)

def normalize_ndarray(X, axis=99, dtype=np.float32):
    X = X.astype(np.float32)
    n_row, n_column = X.shape
    if axis == 99:
        X_mean = np.mean(X)
        X_std = np.std(X)
        Z = (X - X_mean) / X_std
    if axis == 0:
        X_mean = np.mean(X,0).reshape(1,-1)
        X_std = np.std(X,0).reshape(1,-1)
        Z = (X - X_mean) / X_std
    if axis == 1:
        X_mean = np.mean(X,1).reshape(n_row,-1)
        X_std = np.std(X,1).reshape(n_row,-1)
        Z = (X - X_mean) / X_std

    return Z

X = np.arange(12,dtype=np.float32).reshape(6,2)
normalize_ndarray(X,0)

def save_ndarray(X, filename="test.npy"):
    '''
    file_test = open(filename,"wb")
    np.save(X,file_test)
    '''
    pass


def boolean_index(X, condition):
    condition = eval(str("X") + condition)
    return np.where(condition)

X = np.arange(32,dtype=np.float32)
boolean_index(X,"> 6")

def find_nearest_value(X, target_value):
    return X[np.argmin(np.abs(X-target_value))]

X = np.random.uniform(0,1,5)
X
target_value = 0.3
find_nearest_value(X,target_value)

def get_n_largest_values(X, n):
    return X[np.argsort(X[::-1])[:n]]

X = np.random.uniform(0,1,5)
X
np.argsort(X) # 작은 값부터 인덱스를 반환
