
from paraview.simple import *
from paraview import coprocessing


#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# paraview version 5.5.2

#--------------------------------------------------------------
# Global screenshot output options
imageFileNamePadding=5
rescale_lookuptable=False


# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.5.2

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.5.2

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [934, 826]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.OrientationAxesVisibility = 0
      renderView1.CenterOfRotation = [32.0, 32.0, 0.5]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [37.1758835245093, 31.7001128348074, 155.144287234218]
      renderView1.CameraFocalPoint = [37.1758835245093, 31.7001128348074, -19.7176361979913]
      renderView1.CameraParallelScale = 45.2575960475145
      renderView1.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView1.AxesGrid.XTitleFontFile = ''
      renderView1.AxesGrid.YTitleFontFile = ''
      renderView1.AxesGrid.ZTitleFontFile = ''
      renderView1.AxesGrid.XLabelFontFile = ''
      renderView1.AxesGrid.YLabelFontFile = ''
      renderView1.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='random_2d_64_catalyst_%t.png', freq=1, fittoscreen=0, magnification=1, width=934, height=826, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(renderView1)
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'PVD Reader'
      # create a producer from a simulation input
      meshpvd = coprocessor.CreateProducer(datadescription, 'mesh')

      # create a new 'Cell Data to Point Data'
      cellDatatoPointData1 = CellDatatoPointData(Input=meshpvd)
      cellDatatoPointData1.PassCellData = 1

      # create a new 'Annotate Time'
      annotateTime1 = AnnotateTime()
      annotateTime1.Format = 't = %0.2f'

      # create a new 'Slice'
      slice1 = Slice(Input=cellDatatoPointData1)
      slice1.SliceType = 'Plane'
      slice1.SliceOffsetValues = [0.0]

      # init the 'Plane' selected for 'SliceType'
      slice1.SliceType.Origin = [32.0, 32.0, 0.5]
      slice1.SliceType.Normal = [0.0, 0.0, 1.0]

      # create a new 'Contour'
      contour1 = Contour(Input=slice1)
      contour1.ContourBy = ['POINTS', 'data']
      contour1.Isosurfaces = [1.0]
      contour1.PointMergeMethod = 'Uniform Binning'

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from slice1
      slice1Display = Show(slice1, renderView1)

      # get color transfer function/color map for 'data'
      dataLUT = GetColorTransferFunction('data')
      dataLUT.RGBPoints = [-1.0, 0.278431372549, 0.278431372549, 0.858823529412, -0.571, 0.0, 0.0, 0.360784313725, -0.145, 0.0, 1.0, 1.0, 0.287, 0.0, 0.501960784314, 0.0, 0.713, 1.0, 1.0, 0.0, 1.142, 1.0, 0.380392156863, 0.0, 1.571, 0.419607843137, 0.0, 0.0, 2.0, 0.878431372549, 0.301960784314, 0.301960784314]
      dataLUT.ColorSpace = 'RGB'
      dataLUT.ScalarRangeInitialized = 1.0

      # trace defaults for the display properties.
      slice1Display.Representation = 'Surface'
      slice1Display.ColorArrayName = ['CELLS', 'data']
      slice1Display.LookupTable = dataLUT
      slice1Display.LineWidth = 3.0
      slice1Display.OSPRayScaleArray = 'data'
      slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      slice1Display.SelectOrientationVectors = 'None'
      slice1Display.ScaleFactor = 6.4
      slice1Display.SelectScaleArray = 'data'
      slice1Display.GlyphType = 'Arrow'
      slice1Display.GlyphTableIndexArray = 'data'
      slice1Display.GaussianRadius = 0.32
      slice1Display.SetScaleArray = ['POINTS', 'data']
      slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
      slice1Display.OpacityArray = ['POINTS', 'data']
      slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
      slice1Display.DataAxesGrid = 'GridAxesRepresentation'
      slice1Display.SelectionCellLabelFontFile = ''
      slice1Display.SelectionPointLabelFontFile = ''
      slice1Display.PolarAxes = 'PolarAxesRepresentation'

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      slice1Display.ScaleTransferFunction.Points = [-0.554055094718933, 0.0, 0.5, 0.0, 1.65849852561951, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      slice1Display.OpacityTransferFunction.Points = [-0.554055094718933, 0.0, 0.5, 0.0, 1.65849852561951, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      slice1Display.DataAxesGrid.XTitle = 'X'
      slice1Display.DataAxesGrid.YTitle = 'Y'
      slice1Display.DataAxesGrid.ZTitle = 'Z'
      slice1Display.DataAxesGrid.XTitleFontFile = ''
      slice1Display.DataAxesGrid.XTitleBold = 1
      slice1Display.DataAxesGrid.YTitleFontFile = ''
      slice1Display.DataAxesGrid.YTitleBold = 1
      slice1Display.DataAxesGrid.ZTitleFontFile = ''
      slice1Display.DataAxesGrid.ZTitleBold = 1
      slice1Display.DataAxesGrid.XLabelFontFile = ''
      slice1Display.DataAxesGrid.XLabelBold = 1
      slice1Display.DataAxesGrid.YLabelFontFile = ''
      slice1Display.DataAxesGrid.YLabelBold = 1
      slice1Display.DataAxesGrid.ZLabelFontFile = ''
      slice1Display.DataAxesGrid.ZLabelBold = 1

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
      slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
      slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
      slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # show data from contour1
      contour1Display = Show(contour1, renderView1)

      # trace defaults for the display properties.
      contour1Display.Representation = 'Surface'
      contour1Display.ColorArrayName = ['POINTS', '']
      contour1Display.DiffuseColor = [0.0, 0.0, 0.0]
      contour1Display.LineWidth = 3.0
      contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      contour1Display.SelectOrientationVectors = 'None'
      contour1Display.ScaleFactor = 4.24923191070557
      contour1Display.SelectScaleArray = 'data'
      contour1Display.GlyphType = 'Arrow'
      contour1Display.GlyphTableIndexArray = 'data'
      contour1Display.GaussianRadius = 0.212461595535278
      contour1Display.SetScaleArray = [None, '']
      contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
      contour1Display.OpacityArray = [None, '']
      contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
      contour1Display.DataAxesGrid = 'GridAxesRepresentation'
      contour1Display.SelectionCellLabelFontFile = ''
      contour1Display.SelectionPointLabelFontFile = ''
      contour1Display.PolarAxes = 'PolarAxesRepresentation'

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      contour1Display.DataAxesGrid.XTitleFontFile = ''
      contour1Display.DataAxesGrid.YTitleFontFile = ''
      contour1Display.DataAxesGrid.ZTitleFontFile = ''
      contour1Display.DataAxesGrid.XLabelFontFile = ''
      contour1Display.DataAxesGrid.YLabelFontFile = ''
      contour1Display.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
      contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
      contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
      contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # show data from annotateTime1
      annotateTime1Display = Show(annotateTime1, renderView1)

      # trace defaults for the display properties.
      annotateTime1Display.FontFile = ''
      annotateTime1Display.Bold = 1
      annotateTime1Display.FontSize = 14

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for dataLUT in view renderView1
      dataLUTColorBar = GetScalarBar(dataLUT, renderView1)
      dataLUTColorBar.WindowLocation = 'AnyLocation'
      dataLUTColorBar.Position = [0.883898446170921, 0.112155721512035]
      dataLUTColorBar.Title = 'data'
      dataLUTColorBar.ComponentTitle = ''
      dataLUTColorBar.TitleFontFile = ''
      dataLUTColorBar.TitleBold = 1
      dataLUTColorBar.LabelFontFile = ''
      dataLUTColorBar.LabelBold = 1
      dataLUTColorBar.RangeLabelFormat = '%-#6.1f'
      dataLUTColorBar.ScalarBarLength = 0.777973972590605

      # set color bar visibility
      dataLUTColorBar.Visibility = 1

      # show color legend
      slice1Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get opacity transfer function/opacity map for 'data'
      dataPWF = GetOpacityTransferFunction('data')
      dataPWF.Points = [-1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
      dataPWF.ScalarRangeInitialized = 1

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(annotateTime1)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'mesh': [1, 1, 1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(False, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor
    if datadescription.GetForceOutput() == True:
        # We are just going to request all fields and meshes from the simulation
        # code/adaptor.
        for i in range(datadescription.GetNumberOfInputDescriptions()):
            datadescription.GetInputDescription(i).AllFieldsOn()
            datadescription.GetInputDescription(i).GenerateMeshOn()
        return

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
