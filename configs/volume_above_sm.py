import numpy as np, matplotlib.pyplot as plt
from vtk.util.numpy_support import *
from vtk import vtkDataObject, vtkCompositeDataSet

# default values of control parameters
threshold = 0.5
mesh = ''
array = ''
cen = vtkDataObject.POINT
out_file = 'area_above.png'
times = []
area_above = []

def pt_centered(c):
  return c == vtkDataObject.POINT

def Execute(adaptor):
  # get the mesh and arrays we need
  dobj = adaptor.GetMesh(mesh, False)
  adaptor.AddArray(dobj, mesh, cen, array)
  adaptor.AddGhostCellsArray(dobj, mesh)
  time = adaptor.GetDataTime()

  # compute area above over local blocks
  area = 0.
  it = dobj.NewIterator()
  while not it.IsDoneWithTraversal():
    # get the local data block and its props
    blk = it.GetCurrentDataObject()
    dim = [i-j for i,j in zip(blk.GetDimensions(), \
      [0]*3 if pt_centered(cen) else [1]*3)]

    # get the array container
    atts = blk.GetPointData() if pt_centered(cen) \
       else blk.GetCellData()

    # get the data and ghost arrays
    data = vtk_to_numpy(atts.GetArray(array))
    ghost = vtk_to_numpy(atts.GetArray('vtkGhostType'))
    ghost.shape = data.shape = (dim[1], dim[0])

    # compute the area above
    ii = np.where((data > threshold) & (ghost == 0))
    area += len(ii[0])*np.prod(blk.GetSpacing())

    it.GoToNextItem()

  # compute global area
  area = comm.reduce(area, root=0, op=MPI.SUM)

  # rank zero writes the result
  if comm.Get_rank() == 0:
    times.append(time)
    area_above.append(area)

def Finalize():
  if comm.Get_rank() == 0:
    plt.plot(times, area_above, 'b-', linewidth=2)
    plt.xlabel('time')
    plt.ylabel('area')
    plt.title('Area Above %0.2f'%(threshold))
    plt.savefig(out_file)
  return 0
