<script lang="ts">
export const description = "Enrollment history page"
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
  TableHeader,
  TableRow,
  TableHead,
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
  MoreHorizontal,
  User,
  Layers,
  Calendar,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy enrollment history data
const history = ref([
  {
    id: 1,
    student: "John Mark Rivera",
    grade: "Grade 11",
    section: "STEM A",
    action: "Enrolled",
    date: "2024-01-12",
    time: "08:45 AM",
    color: "bg-green-500",
  },
  {
    id: 2,
    student: "Andrea Lopez",
    grade: "Grade 11",
    section: "HUMSS B",
    action: "Pending Enrollment",
    date: "2024-01-11",
    time: "02:20 PM",
    color: "bg-yellow-500",
  },
  {
    id: 3,
    student: "Rico Delos Santos",
    grade: "Grade 12",
    section: "ABM A",
    action: "Enrollment Updated",
    date: "2024-01-10",
    time: "10:15 AM",
    color: "bg-blue-500",
  },
  {
    id: 4,
    student: "Kyla Francisco",
    grade: "Grade 12",
    section: "GAS C",
    action: "Dropped",
    date: "2024-01-08",
    time: "04:10 PM",
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
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Enrollment History</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Enrollment History</h2>
            <p class="text-sm text-muted-foreground">
              Review the log of all student enrollment actions.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <History class="h-4 w-4" />
            Export Logs
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>History Logs</CardTitle>
            <CardDescription>
              View timestamps and actions for all enrollment changes.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search history..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-56">Student</TableHead>
                  <TableHead>Grade & Section</TableHead>
                  <TableHead>Action</TableHead>
                  <TableHead>Date</TableHead>
                  <TableHead>Time</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="log in history"
                  :key="log.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Student -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <User class="h-4 w-4 text-muted-foreground" />
                      <span class="font-medium">{{ log.student }}</span>
                    </div>
                  </TableCell>

                  <!-- Grade & Section -->
                  <TableCell class="flex flex-col gap-0.5">
                    <span class="text-sm text-muted-foreground">{{ log.grade }}</span>
                    <div class="flex items-center gap-1 text-muted-foreground text-xs">
                      <Layers class="h-3 w-3" />
                      <span>{{ log.section }}</span>
                    </div>
                  </TableCell>

                  <!-- Action -->
                  <TableCell>
                    <Badge :class="log.color">{{ log.action }}</Badge>
                  </TableCell>

                  <!-- Date -->
                  <TableCell>
                    <div class="flex items-center gap-1">
                      <Calendar class="h-3 w-3 text-muted-foreground" />
                      <span>{{ log.date }}</span>
                    </div>
                  </TableCell>

                  <!-- Time -->
                  <TableCell class="text-muted-foreground">
                    {{ log.time }}
                  </TableCell>

                  <!-- Actions -->
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
