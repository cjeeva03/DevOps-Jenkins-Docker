import jenkins.model.*
import hudson.PluginManager
import hudson.model.UpdateCenter

def instance = Jenkins.getInstance()
def pluginManager = instance.getPluginManager()
def updateCenter = instance.getUpdateCenter()

def plugins = [
    "git",
    "workflow-aggregator",
    "docker-plugin",
    "blueocean",
    "credentials-binding"
]

plugins.each { plugin ->
    if (!pluginManager.getPlugin(plugin)) {
        def pluginInstall = updateCenter.getPlugin(plugin)
        if (pluginInstall) {
            pluginInstall.deploy()
        }
    }
}
