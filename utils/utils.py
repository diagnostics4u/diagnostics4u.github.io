"""Utils.
Adapted from yuan-xiaohan/Slice-mask-based-3D-Cardiac-Shape-Reconstruction.
"""
PCA_NUM = 50

def PCA_operation(file_base):
    """
    Output：
    # X_aver: (v_num, 3)
    # X_new: (v_num*3, k)
    # VT: (k, n)
    # X_pca_ratio: (k, )
    """

    aver_dir = os.path.join(file_base, "aver.obj")
    VT_dir = os.path.join(file_base, "VT.txt")
    var_ratio_dir = os.path.join(file_base, "pca_ratio.txt")

    # get mean obj
    aver_v, face = obj_read(aver_dir)
    VT = np.loadtxt(VT_dir, dtype=np.float)
    var_ratio = np.loadtxt(var_ratio_dir, dtype=np.float)
    # print(var_ratio.shape)
    return aver_v, face, VT, var_ratio


def reconstruction(pca_coff, VT, aver_v):
    """
    # VT: (k, n), n = v_num * 3
    # pca_coff: (m, k)
    # aver: (v_num, 3)
    # m_reconstruct:(m, v_num, 3)
    """
    m_reconstruct = np.dot(pca_coff, VT)  # X = X_new * VT, (m, v_num * 3)
    m_reconstruct = np.repeat(np.expand_dims(aver_v, axis=0), pca_coff.shape[0], axis=0) + np.reshape(m_reconstruct,
                                                                                                      [pca_coff.shape[0],
                                                                                                       aver_v.shape[0],
                                                                                                       aver_v.shape[1]])
    return m_reconstruct

def normalization2(image, max, min):
    """Normalization to range of [min, max]
    Args :
        image : numpy array of image
        mean :
    Return :
        image : numpy array of image with values turned into standard scores
    """
    image_new = (image - np.min(image))*(max - min)/(np.max(image)-np.min(image)) + min
    return image_new


def obj_read(obj_path):
    # read obj file and get vertices and faces
    with open(obj_path) as file:
        vertices = []
        faces = []
        while 1:
            line = file.readline()
            if not line:
                break
            strs = line.split(" ")
            if strs[0] == "v":
                vertices.append((float(strs[1]), float(strs[2]), float(strs[3])))
            if strs[0] == "vt":
                break
            if strs[0] == "f":
                faces.append(
                    (int(strs[1].split('//')[0]), int(strs[2].split('//')[0]), int(strs[3].split('//')[0])))
    vertices = np.array(vertices)  # in matrix form
    faces = np.array(faces)
    return vertices, faces


def obj_write(obj_path, vertices, faces):
    with open(obj_path, "w") as file:
        file.write("# " + str(vertices.shape[0]) + " vertices, " + str(faces.shape[0]) + " faces" + "\n")
        # write vertices
        for i in range(vertices.shape[0]):
            file.write("v ")
            file.write(str(float("{0:.6g}".format(vertices[i, 0]))) + " ")
            file.write(str(float("{0:.6g}".format(vertices[i, 1]))) + " ")
            file.write(str(float("{0:.6g}".format(vertices[i, 2]))) + " ")
            file.write("\n")
        # write faces
        for i in range(faces.shape[0]):
            file.write("f ")
            file.write(str(int(faces[i, 0])) + " ")
            file.write(str(int(faces[i, 1])) + " ")
            file.write(str(int(faces[i, 2])) + " ")
            file.write("\n")
