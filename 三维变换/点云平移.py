from copy import deepcopy
import open3d as o3d

if __name__ == '__main__':
    coord = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.6, origin=[0, 0, 0])  # 设置坐标系
    file_path = 'rabbit.pcd'
    pcd = o3d.io.read_point_cloud(file_path)
    pcd.paint_uniform_color([0.5, 0.5, 0.5])  # 指定显示为灰色
    # x方向平移
    pcd1 = deepcopy(pcd)
    pcd1.translate((0.5, 0, 0), relative=True)
    pcd1.paint_uniform_color([1, 0, 0])  # 指定显示为红色
    # y方向平移
    pcd2 = deepcopy(pcd)
    pcd2.translate((0, 0.5, 0), relative=True)
    pcd2.paint_uniform_color([0, 1, 0])  # 指定显示为绿色
    # z方向平移
    pcd3 = deepcopy(pcd)
    pcd3.translate((0, 0, 0.5), relative=True)
    pcd3.paint_uniform_color([0, 0, 1])  # 指定显示为蓝色
    # xyz方向均平移
    pcd4 = deepcopy(pcd)
    pcd4.translate((0.5, 0.5, 0.5), relative=True)
    pcd4.paint_uniform_color([0, 1, 1])  # 指定显示为天蓝色
    # 点云显示
    o3d.visualization.draw_geometries([coord, pcd, pcd1, pcd2, pcd3, pcd4],
                                      window_name="点云平移",
                                      point_show_normal=False,
                                      width=800,  # 窗口宽度
                                      height=600)  # 窗口高度
