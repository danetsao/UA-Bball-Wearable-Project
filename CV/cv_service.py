# This file will contain main logic for cv operations

from utils import read_video, save_video
from trackers import Tracker
import numpy as np
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
import os
#from camera_movement_estimator import CameraMovementEstimator
#from view_transformer import ViewTransformer
#from speed_and_distance_estimator import SpeedAndDistance_Estimator
    
def main(input_video_path):
     # Read Video
    video_frames, fps = read_video('input_videos/' + input_video_path)

    # Initialize Tracker
    tracker = Tracker('models/models-med/best.pt')

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    # Get object positions 
    tracker.add_position_to_tracks(tracks)

    # Interpolate missing ball positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    tracks['players'][0])
    
    for frame_num, player_track in enumerate(tracks['players']):
        #print(f'TEAMS for frame {frame_num}')
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            #print(f'Player ID: {player_id} \t Team: {team}')
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    
    # Assign Ball Acquisition
    player_assigner = PlayerBallAssigner()
    team_ball_control= []
    for frame_num, player_track in enumerate(tracks['players']):
        print('\nframe_num: ', frame_num)
        try:
            ball_bbox = tracks['ball'][frame_num][1]['bbox']

            assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

            if assigned_player != -1:
                print('Successfully assigned ball to player + team...')
                print(tracks['players'][frame_num][assigned_player]['team'])
                tracks['players'][frame_num][assigned_player]['has_ball'] = True
                team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
            else:
                if len(team_ball_control) < 1:
                    team_ball_control.append(3)
                else:
                    team_ball_control.append(team_ball_control[-1])
                #team_ball_control.append(team_ball_control[-1])
        except: 
            print('Excepted...')
            team_ball_control.append(1)
            continue
    team_ball_control = np.array(team_ball_control)


    # Draw output 
    ## Draw object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)

    #print('============ __tracks =============')
    #print(tracks)

    #print('================= _ball_tracks ============')
    #print(tracks['ball'])

    base_name, ext = os.path.splitext(input_video_path)
    output_dir = 'output_videos'
    output_path = os.path.join(output_dir, f"{base_name}{ext}")

    # If the output path exists, save the file with a slightly different name
    count = 1
    while os.path.exists(output_path):
        output_path = os.path.join('output_videos', f"{base_name}_{count}{ext}")
        count += 1

    # Save video
    save_video(output_video_frames, output_path, fps)
    return output_path

if __name__ == '__main__':
    main('duke.mp4')