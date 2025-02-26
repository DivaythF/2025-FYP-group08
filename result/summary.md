# Projects in Data Science (2025)

# 1. Exploration of the Data/ Summary of the Data:

Dataset Overview
The dataset consists of 200 images of skin moulds.
Each image has been annotated with a hair presence rating:

0 = No hair

1 = Some hair

2 = A lot of hair

The primary goal is to develop an algorithm to remove hair from images, enabling better differentiation between cancerous and non-cancerous moulds.
 #  Summary Statistics:

The group uniformly agreed on the hair annotation for 119 pictures (59.5%), with an average agreement of 89.0%. The lowest agreement was 20% for the picture img_0925.png.

# Image Quality & Variability:

The dataset contains images of varying resolutions, lighting conditions, and skin tones.

Some images have darker or lighter backgrounds, which might impact segmentation models.

Hair thickness and density vary across images with ratings 1 and 2.

# Potential Challenges:

Hair thickness variation: Some images may contain thin, scattered hair, while others have dense, overlapping hair.

Skin tone variations: The effectiveness of hair removal may differ for lighter vs. darker skin tones.

Low-contrast images: Some moulds blend into the skin, making segmentation harder.

# 2. Annotation of the Picture:
   
As a group we agreed to rate the various datasets based on the number of hairs that were present on the image and not solely on the lesions.
   
 Below are some examples of data were we collectively agreed had the same ratings:
   
  ![img_0917](https://github.com/user-attachments/assets/3e886e7e-c603-42fd-8662-dd8d6a1d2aa7)
 - We agreed that this image had a rating of 1 due to the presence of some hair.
   
 ![img_0918](https://github.com/user-attachments/assets/73e4147b-0fce-45ba-9e3a-ed223c744dec)
 - We gave this a rating of 2 because it contains a lot of hair.
  
 ![img_0919](https://github.com/user-attachments/assets/6992880a-4b9e-438c-9d20-fd3b4082a3ce)
 - A rating of 0 was given because there was no hair found.

##  Disagreement:
   
![img_0925](https://github.com/user-attachments/assets/90367a09-a4d6-4bf7-8e68-04e372d1718c)
 
-  With this particular image, the group had 3 different ratings on the image. As mentioned above, there was an agreement to rate the number of hairs present in the image but clearly some of us also focused on the image present on the lesion and therefore disregarded the hair present which we assumed to be the persons actual hair. 


# 4. Segmentation of the Hair
   ## First Test Case
   
   Original Picture:
   
   ![image](https://github.com/user-attachments/assets/989d4686-10df-409e-be98-bcfd3edd003b)

   Modified Picture:
   
   ![image](https://github.com/user-attachments/assets/c19813cf-3c6c-47dc-a315-5be02f060c22)

- Tested the hair removal function with this picture.
- The original image had significant hair and was rated a two by all group members.
- The function effectively removed dark hair but struggled with white hair.
- A drawback is the removal of darker spots on the mole, which may affect color and shape analysis.

## Some issues with the hair removal code

For this image, we all agreed that it had no hair, but due to some skin condition, the hair removal code altered it anyway, significantly affecting the lesion itself and possibly making it impossible to accurately diagnose.
![merged_919](https://github.com/user-attachments/assets/3928b0bd-29dd-45ed-bed8-21e4b45a76da)

Also another case where it actually had a lot of hair (rating 2 by all of us). We can see that probably because the hair has similar colour with the lesion, it doesn't really remove the hair on top of it, and also seems to fuse them together.
![merged_1116](https://github.com/user-attachments/assets/39fd7d4e-7609-4ce3-80a7-d4f665c614eb)




