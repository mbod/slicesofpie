

.. _sphx_glr_auto_examples_02_plotting_plot_seaborn2.py:


Seaborn example
===============

Preview the capture of seaborn styles in plots




.. image:: /auto_examples/02_plotting/images/sphx_glr_plot_seaborn2_001.png
    :align: center





.. code-block:: python

    # Author: Michael Waskom
    # License: BSD 3 clause

    from __future__ import division, absolute_import, print_function


    import numpy as np
    import seaborn as sns

    # Enforce the use of default set style
    #sns.set(style="darkgrid", palette="Set2")

    # Create a noisy periodic dataset
    sines = []
    rs = np.random.RandomState(8)
    for _ in range(15):
        x = np.linspace(0, 30 / 2, 30)
        y = np.sin(x) + rs.normal(0, 1.5) + rs.normal(0, .3, 30)
        sines.append(y)

    # Plot the average over replicates with bootstrap resamples
    sns.tsplot(sines, err_style="boot_traces", n_boot=500)

**Total running time of the script:** ( 0 minutes  0.418 seconds)



.. container:: sphx-glr-footer


  .. container:: sphx-glr-download

     :download:`Download Python source code: plot_seaborn2.py <plot_seaborn2.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: plot_seaborn2.ipynb <plot_seaborn2.ipynb>`

.. rst-class:: sphx-glr-signature

    `Generated by Sphinx-Gallery <https://sphinx-gallery.readthedocs.io>`_
