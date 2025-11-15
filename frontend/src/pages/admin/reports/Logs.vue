<script lang="ts">
export const description = "Activity logs report"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"

import {
  Table,
  TableHead,
  TableRow,
  TableHeader,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuItem,
} from "@/components/ui/dropdown-menu"

import {
  History,
  User,
  Settings,
  FileDown,
  Printer,
  MoreHorizontal,
  ShieldCheck,
  Trash2,
  Pencil,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy activity log entries
const logs = ref([
  {
    id: 1,
    action: "Created Student Record",
    module: "Students",
    user: "Maria Santos (Registrar)",
    timestamp: "2024-01-12 08:25 AM",
    icon: Pencil,
    status: "Success",
    color: "bg-green-500",
  },
  {
    id: 2,
    action: "Deleted Section GAS B",
    module: "Sections",
    user: "Admin (Superuser)",
    timestamp: "2024-01-11 09:10 AM",
    icon: Trash2,
    status: "Warning",
    color: "bg-yellow-500",
  },
  {
    id: 3,
    action: "Logged In",
    module: "System",
    user: "Juan Dela Cruz (Teacher)",
    timestamp: "2024-01-11 07:02 AM",
    icon: ShieldCheck,
    status: "Success",
    color: "bg-blue-500",
  },
  {
    id: 4,
    action: "Updated Grades",
    module: "Grades",
    user: "Ana Reyes (Teacher)",
    timestamp: "2024-01-10 04:45 PM",
    icon: Settings,
    status: "Success",
    color: "bg-green-500",
  },
  {
    id: 5,
    action: "Failed Login Attempt",
    module: "System",
    user: "Unknown User",
    timestamp: "2024-01-10 01:15 AM",
    icon: ShieldCheck,
    status: "Failed",
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/reports">Reports</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Activity Logs</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        
        <!-- Top Section -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Activity Logs</h2>
            <p class="text-sm text-muted-foreground">
              Track user actions and system activity across the platform.
            </p>
          </div>

          <div class="flex gap-2">
            <Button variant="secondary" class="flex items-center gap-2">
              <Printer class="h-4 w-4" />
              Print
            </Button>
            <Button class="flex items-center gap-2">
              <FileDown class="h-4 w-4" />
              Export Logs
            </Button>
          </div>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>System Activity Logs</CardTitle>
            <CardDescription>
              View the log of all administrative and user actions.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search logs..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Action</TableHead>
                  <TableHead>Module</TableHead>
                  <TableHead>User</TableHead>
                  <TableHead>Timestamp</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="log in logs"
                  :key="log.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Action -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <component :is="log.icon" class="h-4 w-4 text-muted-foreground" />
                      <span class="font-medium">{{ log.action }}</span>
                    </div>
                  </TableCell>

                  <!-- Module -->
                  <TableCell class="text-muted-foreground">
                    {{ log.module }}
                  </TableCell>

                  <!-- User -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <User class="h-4 w-4 text-muted-foreground" />
                      {{ log.user }}
                    </div>
                  </TableCell>

                  <!-- Timestamp -->
                  <TableCell>
                    <div class="text-muted-foreground">
                      {{ log.timestamp }}
                    </div>
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge :class="log.color">
                      {{ log.status }}
                    </Badge>
                  </TableCell>

                  <!-- Table Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>View Details</DropdownMenuItem>
                        <DropdownMenuItem>Flag for Review</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Delete Log Entry
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>

                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
