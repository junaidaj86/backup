
| Sl.No | Issues | Solution |
| ---- | ---- | ---- |
| 1 | **New PV and PVCs generation**: caused a disconnection from existing metadata, impacting service availability. | Services were reattached with older PV’s Manually |
| 2 | **New Cluster ID’s**: Resulted in Crash loop state. | Adjustment of Kafka.propertiesfiles was necessary to remap the clusters Manually |
| 3 | **IP shortage:** Pods were stuck in Pending state | Using Warm IP properties IP usage was managed |
| 4 | **Control Centre is still non-functional** | Working with Confluent team -ticket raised |
