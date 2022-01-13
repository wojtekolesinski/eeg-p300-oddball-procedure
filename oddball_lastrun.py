#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Jan 13 19:25:56 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'oddball'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/wojtek/UW/3/eeg/oddball/oddball_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='\n\n\n\nWitaj w naszym eksperymencie!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
countdown5 = visual.TextStim(win=win, name='countdown5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
countdown4 = visual.TextStim(win=win, name='countdown4',
    text='\n\n\nPróba rozpocznie się za 4',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
countdown3 = visual.TextStim(win=win, name='countdown3',
    text='\n\n\nPróba rozpocznie się za 3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
countdown2 = visual.TextStim(win=win, name='countdown2',
    text='\n\n\nPróba rozpocznie się za 2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
countdown1 = visual.TextStim(win=win, name='countdown1',
    text='\n\n\nPróba rozpocznie się za 1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "oddball"
oddballClock = core.Clock()
text_ = visual.TextStim(win=win, name='text_',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp = keyboard.Keyboard()
blank_screen = visual.ImageStim(
    win=win,
    name='blank_screen', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
countdown5.setText('\n\n\nPróba rozpocznie się za 5')
# keep track of which components have finished
introComponents = [text, countdown5, countdown4, countdown3, countdown2, countdown1]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *countdown5* updates
    if countdown5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        countdown5.frameNStart = frameN  # exact frame index
        countdown5.tStart = t  # local t and not account for scr refresh
        countdown5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown5, 'tStartRefresh')  # time at next scr refresh
        countdown5.setAutoDraw(True)
    if countdown5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown5.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            countdown5.tStop = t  # not accounting for scr refresh
            countdown5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown5, 'tStopRefresh')  # time at next scr refresh
            countdown5.setAutoDraw(False)
    
    # *countdown4* updates
    if countdown4.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        countdown4.frameNStart = frameN  # exact frame index
        countdown4.tStart = t  # local t and not account for scr refresh
        countdown4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown4, 'tStartRefresh')  # time at next scr refresh
        countdown4.setAutoDraw(True)
    if countdown4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            countdown4.tStop = t  # not accounting for scr refresh
            countdown4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown4, 'tStopRefresh')  # time at next scr refresh
            countdown4.setAutoDraw(False)
    
    # *countdown3* updates
    if countdown3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        countdown3.frameNStart = frameN  # exact frame index
        countdown3.tStart = t  # local t and not account for scr refresh
        countdown3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown3, 'tStartRefresh')  # time at next scr refresh
        countdown3.setAutoDraw(True)
    if countdown3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            countdown3.tStop = t  # not accounting for scr refresh
            countdown3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown3, 'tStopRefresh')  # time at next scr refresh
            countdown3.setAutoDraw(False)
    
    # *countdown2* updates
    if countdown2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        countdown2.frameNStart = frameN  # exact frame index
        countdown2.tStart = t  # local t and not account for scr refresh
        countdown2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown2, 'tStartRefresh')  # time at next scr refresh
        countdown2.setAutoDraw(True)
    if countdown2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            countdown2.tStop = t  # not accounting for scr refresh
            countdown2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown2, 'tStopRefresh')  # time at next scr refresh
            countdown2.setAutoDraw(False)
    
    # *countdown1* updates
    if countdown1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        countdown1.frameNStart = frameN  # exact frame index
        countdown1.tStart = t  # local t and not account for scr refresh
        countdown1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(countdown1, 'tStartRefresh')  # time at next scr refresh
        countdown1.setAutoDraw(True)
    if countdown1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > countdown1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            countdown1.tStop = t  # not accounting for scr refresh
            countdown1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(countdown1, 'tStopRefresh')  # time at next scr refresh
            countdown1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('countdown5.started', countdown5.tStartRefresh)
thisExp.addData('countdown5.stopped', countdown5.tStopRefresh)
thisExp.addData('countdown4.started', countdown4.tStartRefresh)
thisExp.addData('countdown4.stopped', countdown4.tStopRefresh)
thisExp.addData('countdown3.started', countdown3.tStartRefresh)
thisExp.addData('countdown3.stopped', countdown3.tStopRefresh)
thisExp.addData('countdown2.started', countdown2.tStartRefresh)
thisExp.addData('countdown2.stopped', countdown2.tStopRefresh)
thisExp.addData('countdown1.started', countdown1.tStartRefresh)
thisExp.addData('countdown1.stopped', countdown1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "oddball"-------
    continueRoutine = True
    # update component parameters for each repeat
    from numpy.random import uniform
    
    text_duration = .05 + uniform() * .1
    x = 1.3 + uniform() * .5
    image.setImage(photo)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    oddballComponents = [text_, image, key_resp, blank_screen]
    for thisComponent in oddballComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    oddballClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "oddball"-------
    while continueRoutine:
        # get current time
        t = oddballClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=oddballClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_* updates
        if text_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_.frameNStart = frameN  # exact frame index
            text_.tStart = t  # local t and not account for scr refresh
            text_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_, 'tStartRefresh')  # time at next scr refresh
            text_.setAutoDraw(True)
        if text_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_.tStartRefresh + text_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_.tStop = t  # not accounting for scr refresh
                text_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_, 'tStopRefresh')  # time at next scr refresh
                text_.setAutoDraw(False)
        if text_.status == STARTED:  # only update if drawing
            text_.setText(rune
, log=False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
        
        # *blank_screen* updates
        if blank_screen.status == NOT_STARTED and tThisFlip >= text_duration-frameTolerance:
            # keep track of start time/frame for later
            blank_screen.frameNStart = frameN  # exact frame index
            blank_screen.tStart = t  # local t and not account for scr refresh
            blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_screen, 'tStartRefresh')  # time at next scr refresh
            blank_screen.setAutoDraw(True)
        if blank_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_screen.tStartRefresh + x-frameTolerance:
                # keep track of stop time/frame for later
                blank_screen.tStop = t  # not accounting for scr refresh
                blank_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_screen, 'tStopRefresh')  # time at next scr refresh
                blank_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in oddballComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "oddball"-------
    for thisComponent in oddballComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_duration', text_duration)
    trials.addData('text_.started', text_.tStartRefresh)
    trials.addData('text_.stopped', text_.tStopRefresh)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('blank_screen.started', blank_screen.tStartRefresh)
    trials.addData('blank_screen.stopped', blank_screen.tStopRefresh)
    # the Routine "oddball" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
