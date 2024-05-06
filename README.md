# Flat to Fat: 3D model reconstruction using NeRFs

## Abstract
In an era defined by the growing demand for immersive digital experiences, the necessity for precise and efficient 3D modelling techniques has become critical, particularly in domains such as E-commerce, animations, virtual reality, and more. Conventional techniques that rely on 2D video information have not been able to produce accurate 3D representations as they frequently fall short of capturing the subtleties of lighting, texture, and shape that are essential for realistic modeling. To address this limitation, we propose a novel approach that leverages Neural Radiance Fields (NeRFs) to directly infer the geometry and appearance of a scene from inputs, thereby facilitating the generation of 3D models. Our approach works by analyzing a series of successive two-dimensional pictures of an item taken from different perspectives. Our findings highlight how NeRFs may improve the integrity of 3D modeling and view synthesis, where precise scene reconstruction can enhance the user experience.

## Introduction
Presenting products in the most appealing way is essential in various industries, particularly in light of the growth of e-commerce. However, static image-based techniques often fall short in fully capturing the fine features and overall details of products. Recent advancements in computer vision have opened up new opportunities to revolutionize how products are showcased. This research focuses on developing a unique method for reconstructing 3D models from 2D images or videos of products: Neural Radiance Fields (NeRFs). The goal is to provide customers with a more authentic and immersive viewing experience while interacting with items in virtual settings as if they were physically present. The process begins with the creation of a dataset tailored to our requirements. We record videos of the items from different perspectives and transform these videos into a sequence of frames, ensuring comprehensive coverage from every angle. To refine the dataset, we utilize the rembg module to remove backgrounds from all frames, retaining only relevant information for 3D model reconstruction. Our objective is to leverage Neural Network layers for the reconstruction process while maintaining a high level of realism in the generated 3D models. In this research, we present our methodology for 3D model reconstruction from 2D images using NeRFs, specifically designed for various industries. We describe the procedures for creating a dataset, involving video capture, frame extraction, and background removal. We illustrate the efficiency of our approach in generating realistic 3D models of products through experimental evaluation and validation. Additionally, we discuss how our work may impact e-commerce platforms, where these 3D models could revolutionize online shopping by providing users with a more immersive and realistic perspective of the items.

## Dataset Creation and Pre-processing
### Dataset Creation
In this research, as existing datasets do not fully meet our requirements, we undertake the task of creating our own dataset. To achieve this, we capture videos of objects or scenes from multiple viewpoints, ensuring comprehensive coverage. These videos are then processed to extract individual frames using ffmpeg, resulting in a sequence of images that form the basis of our dataset.
![Original input](![image](https://github.com/sreejith2612/Neural-Radiance-Field/assets/67188299/50e5d8d3-3b47-470d-9aa2-6e3ce54860e6)
 "Video to sequence of frames")

### Data Pre-processing
In our research, we perform data pre-processing techniques such as background removal and computing values of pose, images, and focal parameters.

![Data Pre-processing](![image](https://github.com/sreejith2612/Neural-Radiance-Field/assets/67188299/ca7ba5b7-81ed-47aa-8e56-0e430b583ce1)
 "Background removal from Frames")

## Proposed Solution
Our primary objective in developing the proposed project was to revolutionize the process of 3D reconstruction from 2D images, aiming to produce highly realistic 3D models across various domains. The project utilizes a combination of ray sampling, neural network processing, and volume rendering techniques to achieve robust and photorealistic 3D reconstruction from 2D images.

## Results and Discussion
we proposed changes to the Tiny NeRF (Neural Radiance Fields) implementation, adding two new training strategies to improve the model's performance on image reconstruction tasks. The initial version computed the loss function for only one image per iteration. In contrast, our two proposed techniques try to improve the training process by considering several images at once.

## Conclusion
In this study, we proposed two novel training methods for enhancing the performance of the Tiny NeRF model in image reconstruction tasks. Through experimentation and analysis, we have gained valuable insights into the effectiveness of these methods and their impact on reconstruction quality and training efficiency.
