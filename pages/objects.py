import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

st.title("Objects")

option = st.selectbox('Select a Geometric Shape you would like to display', ('Choose Shape','Diamond', 'Cube', 'Kite' ,'Pyramid'))
if option == 'Choose Shape':
    st.write('Please select an object')
else:
    st.write('You selected:', option)

def plt_basic_object_(points, counter):
    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],triangles=tri,shade=True, cmap=cm.seismic,lw=0.5)

    ax.set_xlim3d(-15, 15)
    ax.set_ylim3d(-15, 15)
    ax.set_zlim3d(-15, 15)

    return fig

def _diamond_(bottom_lower=(0,0,0,), side_length=0, height = 0):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([bottom_lower,
                        bottom_lower + [-3, -3, 0],
                        bottom_lower + [3, -3, 0],
                        bottom_lower + [3, 3, 0], 
                        bottom_lower + [-3, 3, 0], 
                        bottom_lower + [0, 0, -6], 
                        bottom_lower + [-5, 0, 0],
                        bottom_lower + [5, 0, 0],
                        bottom_lower + [3, 2, 2],
                        bottom_lower + [-3, 2, 2],
                        bottom_lower + [3, -2, 2],
                        bottom_lower + [3, -2, 2],
                        bottom_lower + [-4, -2, 2],
                        bottom_lower + [4, -2, 2],
                        bottom_lower])
    return points

def _kite_(bottom_lower=(0, 0, 0), side_length=5, height=5):             
        bottom_lower = np.array(bottom_lower)

        a = side_length/2
        b = np.sqrt(3)*side_length/2
        h = height
        points = np.vstack([
        bottom_lower,
        bottom_lower + [5, side_length, 5],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 5, 5],
        bottom_lower + [3, 3, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, 3, side_length],
        bottom_lower + [side_length,0 ,side_length],
        bottom_lower + [side_length,0 ,side_length],
        bottom_lower, 
    ])
        return points

def _pyramid_(bottom_center=(0, 0, 0)):
    bottom_center = np.array(bottom_center) 

    points = np.vstack([
    bottom_center + [-3, -3, 0],
    bottom_center + [-3, +3, 0],
    bottom_center + [+3, -3, 0],
    bottom_center + [+3, +3, 0],
    bottom_center + [0, 0, +5]
    ])

    return points





if option == 'Pyramid':
    init_pyramid = _pyramid_(bottom_center=(0,0,0))
    points_pyramid2 = tf.constant(init_pyramid, dtype=tf.float32)
    counter = 2
    st.title("Image Translate Pyramid")
    x = st.slider("Enter for x:", -15, 15, 0, step=1,key='my_slider4')
    y = st.slider("Enter for y:", -15, 15, 0, step=1,key='my_slider5')
    z = st.slider("Enter for z:", -15, 15, 0, step=1,key='my_slider6')

    translation = tf.constant([x, y, z], dtype=tf.float32)

    translated_points = points_pyramid2 + translation

    fig2 = plt_basic_object_(translated_points.numpy(), counter)
    st.pyplot(fig2)

elif option == 'Kite':
    init_kite = _kite_(bottom_lower=(0,0,0))
    points_hexagonal_prism = tf.constant(init_kite, dtype=tf.float32)
    counter = 3
    st.title("Image Translate Kite")
    x = st.slider("Enter for x:", -15, 15, 0, step=1,key='my_slider7')
    y = st.slider("Enter for y:", -15, 15, 0, step=1,key='my_slider8')
    z = st.slider("Enter for z:", -15, 15, 0, step=1,key='my_slider9')

    translation = tf.constant([x, y, z], dtype=tf.float32)

    translated_points = points_hexagonal_prism + translation

    fig3 = plt_basic_object_(translated_points.numpy(), counter)
    st.pyplot(fig3)


elif option == 'Diamond':
    init_diamond = _diamond_(bottom_lower=(0,0,0))
    points_heart = tf.constant(init_diamond, dtype=tf.float32)
    counter = 1
    st.title("3d Translation for Diamond")
    x = st.slider("Enter for x:", -15, 15, 0, step=1,key='my_slider1')
    y = st.slider("Enter for y:", -15, 15, 0, step=1,key='my_slider2')
    z = st.slider("Enter for z:", -15, 15, 0, step=1,key='my_slider3')

    translation = tf.constant([x, y, z], dtype=tf.float32)
  
    translated_points = points_heart + translation

    fig1 = plt_basic_object_(translated_points.numpy(), counter)
    st.pyplot(fig1)





   