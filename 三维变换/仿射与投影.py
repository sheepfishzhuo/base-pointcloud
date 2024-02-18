import open3d as o3d
from copy import deepcopy
import numpy as np

if __name__ == '__main__':
    coord = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.8, origin=[0, 0, 0])  # 设置坐标系
    file_path = 'rabbit.pcd'
    pcd = o3d.io.read_point_cloud(file_path)
    pcd.paint_uniform_color([0.5, 0.5, 0.5])  # 指定显示为灰色

    # 仿射变换
    T = np.array([[1, 0, 0, 0.5], [0, 1, 1, 0.5], [0, 0, 1, 0], [0, 0, 0, 1]])
    pcd1 = deepcopy(pcd)
    pcd1.transform(T)
    pcd1.paint_uniform_color([0, 0, 1])  # 指定显示为蓝色

    # 旋转矩阵R+x方向平移0.5个单位
    T = np.array([[0, 0, 1, 0.5], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]])
    pcd2 = deepcopy(pcd)
    pcd2.transform(T)
    pcd2.paint_uniform_color([0, 1, 0])  # 指定显示为绿色

    # y方向平移0.5个单位，并且放大2倍
    T = np.array([[1, 0, 0, 0], [0, 1, 0, 0.5], [0, 0, 1, 0], [0, 0, 0, 0.5]])
    pcd3 = deepcopy(pcd)
    pcd3.transform(T)
    pcd3.paint_uniform_color([1, 0, 0])  # 指定显示为红色

    # 点云显示
    o3d.visualization.draw_geometries([coord, pcd, pcd1, pcd2, pcd3],  # 点云列表
                                      window_name="投影变换",
                                      point_show_normal=False,
                                      width=800,  # 窗口宽度
                                      height=600)  # 窗口高度
