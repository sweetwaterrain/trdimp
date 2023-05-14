from pytracking.evaluation.environment import EnvSettings


def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_path = '/kaggle/input/got10k/test'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_path = ''
    settings.network_path = ''
    settings.nfs_path = '/kaggle/working/trdimp/pytracking/networks'
    settings.otb_path = '/kaggle/input/otb2015/OBT100'
    settings.result_plot_path = ''
    settings.results_path = ''
    settings.segmentation_path = ''
    settings.tn_packed_results_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = ''
    settings.uav_path = ''
    settings.vot_path = '/kaggle/input/vot2013/VOT2013'
    settings.youtubevos_dir = ''

    return settings
