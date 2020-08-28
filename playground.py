import numpy as np
from scipy import spatial

def distance(embeddings1, embeddings2):
    ##### Old
    # dot = np.sum(np.multiply(embeddings1, embeddings2), axis=1)
    # norm = np.linalg.norm(embeddings1, axis=1) * np.linalg.norm(embeddings2, axis=1)
    # similarity = dot / norm
    # dist = np.arccos(similarity) / math.pi

    ###### With `scipy`
    # dist = spatial.distance.cosine(embeddings1, embeddings2)

    ###### Based on `scipy`
    uv = np.average(embeddings1 * embeddings2)
    uu = np.average(np.square(embeddings1))
    vv = np.average(np.square(embeddings2))
    dist = 1.0 - uv / np.sqrt(uu * vv)

    return dist


if __name__ == '__main__':
    print("BLAAAA")

    a = distance( np.array([1, 0, 0]),  np.array([0, 1, 0]))
    print(a) #1.0
    b = distance( np.array([100, 0, 0]),  np.array([0, 1, 0]))
    print(b) # 1.0
    c = distance( np.array([1, 1, 0]),  np.array([0, 1, 0]))
    print(c) # 0.29289321881345254


   ###########################################################
    print(60*"-")
    arr = np.array([1, 2, 3, 4])
    r1 = np.average(arr)
    print("Average of: " + str(arr)  + "  is: " + str(r1))

    r2 = np.square(arr)
    print("Square of: " + str(arr)  + "  is: " + str(r2))

    r3 = np.sqrt(arr)
    print("Sqrt of: " + str(arr)  + "  is: " + str(r3))