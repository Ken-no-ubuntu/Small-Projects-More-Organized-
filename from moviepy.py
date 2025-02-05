from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load the original video
original_video = VideoFileClip("C:\\Users\\jyoji\\Downloads\\IMG_3401.MOV")

# Cut the video into two segments
segment1 = original_video.subclip(0, 20 * 60)  # from beginning to 20 minutes
segment2 = original_video.subclip(50 * 60, original_video.duration)  # from 50 minutes to end

# Concatenate the segments
final_video = concatenate_videoclips([segment1, segment2])

# Write the final video to a file
final_video.write_videofile("C:\\Users\\jyoji\\Downloads\\final_video.MOV")
